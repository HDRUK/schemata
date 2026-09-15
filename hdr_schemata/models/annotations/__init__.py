import copy
import os
from types import SimpleNamespace

import yaml


def dict_to_namespace(d):
    if isinstance(d, dict):
        return SimpleNamespace(**{k: dict_to_namespace(v) for k, v in d.items()})
    elif isinstance(d, list):
        return [dict_to_namespace(item) for item in d]
    else:
        return d


def stitch_namespaces(base_namespace, update_namespace):
    stitched = copy.deepcopy(base_namespace)
    for attr_name, attr_value in update_namespace.__dict__.items():
        base_attr = getattr(stitched, attr_name, None)
        if isinstance(attr_value, SimpleNamespace) and isinstance(base_attr, SimpleNamespace):
            setattr(stitched, attr_name, stitch_namespaces(base_attr, attr_value))
        else:
            setattr(stitched, attr_name, copy.deepcopy(attr_value))
    return stitched


def get_annotations(current_dir, base=None):
    yaml_file_path = os.path.join(current_dir, "config.yaml")

    with open(yaml_file_path, "r") as stream:
        data = yaml.safe_load(stream)
        namespace = dict_to_namespace(data)
        if isinstance(base, SimpleNamespace):
            namespace = stitch_namespaces(base, namespace)
        return namespace


annotations = get_annotations(os.path.dirname(os.path.abspath(__file__)))
