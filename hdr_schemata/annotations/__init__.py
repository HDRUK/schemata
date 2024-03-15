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


def get_annotations():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_file_path = os.path.join(current_dir, "config.yaml")

    with open(yaml_file_path, "r") as stream:
        data = yaml.safe_load(stream)
        return dict_to_namespace(data)


annotations = get_annotations()
