import glob
import json

def sort_versions(versions):
    def version_key(version):
        try:
            return tuple(map(int, (version.split("."))))
        except ValueError:
            return (version.lower(),)
    
    return sorted(versions, key=version_key)

structure = {}
for schema in glob.glob("hdr_schemata/models/**/schema.json", recursive=True):
    items = schema.split("/")
    if len(items) != 5:
        continue
    model = items[2]
    version = items[3]
    if model not in structure:
        structure[model] = []
    structure[model].append(version)

for model in structure:
    structure[model] = sort_versions(structure[model])

json.dump(structure, open("available.json", "w"), indent=6)
