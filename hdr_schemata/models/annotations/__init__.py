import yaml
import os
from types import SimpleNamespace


def dict_to_namespace(d):
    if isinstance(d, dict):
        return SimpleNamespace(**{k: dict_to_namespace(v) for k, v in d.items()})
    elif isinstance(d, list):
        return [dict_to_namespace(item) for item in d]
    else:
        return d


def stitch_namespaces(base_namespace, update_namespace):
    def update_nested(base, update):
        for attr_name, attr_value in update.__dict__.items():
            if isinstance(attr_value, SimpleNamespace):
                base_attr = getattr(base, attr_name, None)
                if isinstance(base_attr, SimpleNamespace):
                    update_nested(base_attr, attr_value)
                else:
                    setattr(base, attr_name, attr_value)
            else:
                setattr(base, attr_name, attr_value)

    stitched_namespace = SimpleNamespace()
    update_nested(stitched_namespace, base_namespace)
    update_nested(stitched_namespace, update_namespace)

    return stitched_namespace


def get_annotations(current_dir, base=None):
    yaml_file_path = os.path.join(current_dir, "config.yaml")

    with open(yaml_file_path, "r") as stream:
        data = yaml.safe_load(stream)
        namespace = dict_to_namespace(data)
        if base and isinstance(base, SimpleNamespace):
            namespace = stitch_namespaces(base, namespace)
        return namespace


annotations = get_annotations(os.path.dirname(os.path.abspath(__file__)))
