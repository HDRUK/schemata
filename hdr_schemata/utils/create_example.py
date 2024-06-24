import json



def get_subItems(item):
    return (
        {subItem["name"]: get_subItems(subItem) for subItem in item["subItems"]}
        if item.get("subItems")
        else " | ".join(item["type"])
    )

def create_example(path):
    data = json.load(open(f"{path}.structure.json"))
    example = {item["name"]: get_subItems(item) for item in data}
    print(json.dumps(example, indent=6))
    with open(f"{path}.example.json", "w") as f:
        json.dump(example, f, indent=6)

create_example("./docs/HDRUK/3.0.0")
