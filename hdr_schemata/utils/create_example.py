import json

data = json.load(open("temp.json"))


def get_subItems(item):
    return (
        {subItem["name"]: get_subItems(subItem) for subItem in item["subItems"]}
        if item.get("subItems")
        else " | ".join(item["type"])
    )


example = {item["name"]: get_subItems(item) for item in data}
print(json.dumps(example, indent=6))
with open("temp2.json", "w") as f:
    json.dump(example, f, indent=6)

# print(json.dumps(data, indent=6))
