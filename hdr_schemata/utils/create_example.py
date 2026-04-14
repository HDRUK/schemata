import json
import datetime
import re
import ast

def get_subItems(item):
    return (
        {subItem["name"]: get_subItems(subItem) for subItem in item["subItems"]}
        if item.get("subItems")
        else " | ".join(item["type"])
    )

def create_template(path):
    data = json.load(open(f"{path}.structure.json"))
    example = {item["name"]: get_subItems(item) for item in data}
    # print(json.dumps(example, indent=6))
    with open(f"{path}.template.json", "w") as f:
        json.dump(example, f, indent=6)

def make_example(item):
    if item["name"] == "structuralMetadata":
        return None
    if item.get("subItems"):
        if item["is_list"]:
            return [{subItem["name"]: make_example(subItem) for subItem in item["subItems"]}]
        else:
            return {subItem["name"]: make_example(subItem) for subItem in item["subItems"]}
    elif "null" in item["type"]:
        return None
    elif item["is_list"]:
        return item["examples"] if item["examples"] else None
    else:
        return item["examples"][0] if item["examples"] else None

def create_example(path):
    data = json.load(open(f"{path}.structure.json"))
    example = {item["name"]: make_example(item) for item in data}
    with open(f"{path}.example.json", "w") as f:
        json.dump(example, f, indent=6)

create_template("./docs/HDRUK/4.0.0")
create_example("./docs/HDRUK/4.0.0")
