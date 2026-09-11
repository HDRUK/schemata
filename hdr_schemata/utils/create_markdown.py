from pydantic import BaseModel, RootModel
import pandas as pd
import copy
import json
import typing
import enum
import os
import importlib
import inspect
from pathlib import Path
from hdr_schemata.utils.markdown_cleaner import clean_markdown_from_json
from hdr_schemata.utils.markdown_cleaner import replace_new_lines_with_breaks

dir_path = os.path.dirname(os.path.realpath(__file__))
REPO_ROOT = Path(dir_path).parent.parent
DOCS_DIR = REPO_ROOT / "docs"

# Families to generate docs for: family_key -> (nav display name, docs subfolder)
DOC_FAMILIES = {
    "GWDM": ("Gateway Data Model (GWDM)", "GWDM"),
    "HDRUK": ("HDRUK", "HDRUK"),
}


def _version_str(version_dir_name: str) -> str:
    """v1_0 -> '1.0', v2_1_2 -> '2.1.2'"""
    return version_dir_name[1:].replace("_", ".")


def _version_sort_key(version_str: str) -> tuple:
    try:
        return tuple(int(x) for x in version_str.split("."))
    except ValueError:
        return (0,)


def extract_type_info(type_hint):
    is_list = False
    is_optional = False
    inner_types = None
    if getattr(type_hint, "__origin__", None) is list:
        is_list = True
        inner_types = type_hint.__args__
    elif getattr(type_hint, "__origin__", None) is typing.Union:
        inner_types = type_hint.__args__
        inner_types_not_none = [
            _type for _type in inner_types if not _type is type(None)
        ]
        is_optional = len(inner_types_not_none) < len(inner_types)

        inner_types = inner_types_not_none
        if is_optional:
            inner_types += ["null"]

        inner_type = inner_types[0]
        is_list = getattr(inner_type, "__origin__", None) is list
        if hasattr(inner_type, "__args__"):
            inner_types = inner_type.__args__

    else:
        inner_types = [type_hint]

    type_names = []
    for _type in inner_types:
        type_name = getattr(_type, "__name__", str(_type))
        try:
            if _type and issubclass(_type, RootModel):
                info = _type.model_json_schema()
                title = info.pop("title")
                type_name += "[" + json.dumps(info).replace('"', "'") + "]"
                # type_name = {title: info}
        except TypeError:
            ...

        if type(_type) == enum.EnumMeta:
            type_name += (
                "["
                + ",".join(
                    [
                        "'" + member.value + "'" if member.value else "null"
                        for member in _type
                    ]
                )
                + "]"
            )

        type_names.append(type_name)

    return is_list, is_optional, type_names, inner_types


def get_fields(structure, model: type[BaseModel]):
    model_hints = typing.get_type_hints(model)
    for name, field in model.model_fields.items():
        if name == "root":
            continue

        t = field.annotation

        _type = model_hints[name]

        is_list, is_optional, type_names, _types = extract_type_info(_type)

        if field.json_schema_extra is not None and "guidance" in field.json_schema_extra:
            guidance = field.json_schema_extra["guidance"]
        else:
            guidance = ""

        value = {
            "name": name,
            "required": field.is_required(),
            "title": field.title,
            "description": field.description,
            "title": field.title,
            "guidance": guidance,
            "examples": field.examples,
            "type": type_names,
            "types": _types,
            "is_list": is_list,
            "is_optional": is_optional,
        }

        while hasattr(t, "__args__"):
            t = t.__args__[0]

        if isinstance(t, type) and issubclass(t, BaseModel):
            subItems = []
            get_fields(subItems, t)
            # Don't ask and I wont lie, but I will run away and cry in the sink.
            if str(t.__name__) == "HealthAndDisease":
                subItems.pop()
                subItems.pop()
            value["subItems"] = subItems

        structure.append(value)


def json_to_markdown(structure, level=2):
    md = ""
    structure = replace_new_lines_with_breaks(structure)
    for field in structure:
        name = field.pop("name")
        subItems = field.pop("subItems", None)
        description = field.pop("description")
        examples = field.pop("examples")

        # Removing the is_optional fields from the markdown docs
        del field["is_optional"]

        if examples:
            examples = "\n".join(["  * " + str(x) for x in examples])
            examples = "Examples: \n\n " + examples
        else:
            examples = ""

        table = ""
        if not subItems:
            table = pd.Series(field).sort_index().to_frame().T.set_index("title")
            table = table.to_markdown()

        heading = "#" * level
        md += rf"""
{heading} {name}

{description}

{table}

{examples}

"""

        if subItems:
            md += json_to_markdown(subItems, level=level + 1)

    return md


def form_structure(data, form, parent=None):
    data = copy.deepcopy(data)
    for item in data:
        k = item.pop("name")
        if parent:
            k = parent + "." + k
        subItems = item.pop("subItems", None)
        if subItems:
            form_structure(subItems, form, parent=k)

        if "structuralMetadata.tables" in k:
            continue

        types = item.pop("types")
        infos = []
        for t in types:
            info = None
            if t == "null":
                continue
            try:
                if "Union" in str(t):
                    options = []
                    for subt in t.__args__:
                        t_sch = subt.model_json_schema()
                        polite_title = t_sch["properties"]["name"]["default"]
                        if subt.__name__ + "SubTypes" in t_sch["$defs"]:
                            dataTypes = t_sch["$defs"][subt.__name__ + "SubTypes"]["enum"]
                            options.append({"title": polite_title, "options": dataTypes})
                        else:
                            dataTypes = t_sch["$defs"]["NotApplicableSubTypes"]
                            options.append({"title": polite_title, "options": ['Not applicable']})

                    info = {"title": t.__name__, "type": "nested", "options": options}
                elif issubclass(t, RootModel):
                    t_sch = t.model_json_schema()
                    # Merge dicts with title and the types info in anyOf
                    if "anyOf" in t_sch:
                        title = {"title": t_sch["title"]}
                        info = {**title, **t_sch["anyOf"][0]}
                    else:
                        info = t_sch
                elif issubclass(t, BaseModel):
                    continue
                else:
                    info = t.__name__
            except:
                ...
            if type(t) == enum.EnumMeta:
                info = {"type": "string", "options": [m.value for m in t]}
                if all(hasattr(m, "label") for m in t):
                    info["option_titles"] = [m.label for m in t]

            if info:
                infos.append(info)

        _ = item.pop("type")

        if isinstance(infos, list):
            # Skip fields where the type is a pydantic type we have defined e.g. "Organisation"
            # because we drill down into the subtypes instead
            if len(infos) == 0:
                continue
            else:
                item["types"] = infos[0]
        else:
            item["types"] = infos
        # location indicates the json path through the schema e.g. summary.abstract
        # provenance.origin.purpose
        item["location"] = k
        form["schema_fields"].append(item)


def _flatten_fields(fields, prefix=""):
    """Recursively flatten nested structure.json into {dotted_path: field_dict}."""
    result = {}
    for field in fields:
        path = f"{prefix}.{field['name']}" if prefix else field['name']
        result[path] = {k: v for k, v in field.items() if k != "subItems"}
        if field.get("subItems"):
            result.update(_flatten_fields(field["subItems"], prefix=path))
    return result


def _diff_structures(old_fields: dict, new_fields: dict):
    old_keys = set(old_fields)
    new_keys = set(new_fields)

    added = sorted(new_keys - old_keys)
    removed = sorted(old_keys - new_keys)

    modified = []
    for key in sorted(old_keys & new_keys):
        old, new = old_fields[key], new_fields[key]
        changes = []
        if old.get("type") != new.get("type"):
            changes.append(f"type `{'|'.join(old.get('type', []))}` → `{'|'.join(new.get('type', []))}`")
        if old.get("required") != new.get("required"):
            changes.append("became required" if new.get("required") else "became optional")
        if old.get("is_list") != new.get("is_list"):
            changes.append("is now a list" if new.get("is_list") else "is no longer a list")
        if changes:
            modified.append((key, changes))

    return added, removed, modified


def generate_change_md(old_version: str, new_version: str, old_structure: list, new_structure: list) -> str:
    old_fields = _flatten_fields(old_structure)
    new_fields = _flatten_fields(new_structure)
    added, removed, modified = _diff_structures(old_fields, new_fields)

    lines = [f"## Changes from {old_version} -> {new_version}\n"]

    if not added and not removed and not modified:
        lines.append("No structural changes detected.\n")
        return "\n".join(lines)

    if added:
        lines.append("### Added\n")
        for path in added:
            field = new_fields[path]
            opt = " *(optional)*" if not field.get("required") else ""
            desc = field.get("description") or field.get("title") or ""
            lines.append(f"- **`{path}`**{opt}: {desc}")
        lines.append("")

    if removed:
        lines.append("### Removed\n")
        for path in removed:
            lines.append(f"- **`{path}`**")
        lines.append("")

    if modified:
        lines.append("### Modified\n")
        for path, changes in modified:
            lines.append(f"- **`{path}`**: {'; '.join(changes)}")
        lines.append("")

    return "\n".join(lines)


def create_markdown(Model, path, name):

    def remove_types(data):
        for d in data:
            d.pop("types")
            if d.get("subItems", None):
                remove_types(d["subItems"])

    structure = []
    get_fields(structure, Model)

    form = {}
    form["schema_fields"] = []
    form["url_regex"] = "^\s*((https?:\/\/)*([a-zA-Z0-9-]+\.?)+[a-zA-Z]{2,}(:\d+)?(\/[^\s]*)?(\n)?)+$"
    form_structure(structure, form)
    with open(f"{path}/{name}.form.json", "w") as f:
        json.dump(form, f, indent=6)

    with open(f"{path}/{name}.structure.json", "w") as f:
        remove_types(structure)
        json.dump(clean_markdown_from_json(structure), f, indent=6)

    md = json_to_markdown(structure)
    with open(f"{path}/{name}.md", "w") as f:
        f.write(md)
    print(f"  docs/{name}")


class _OpaqueYamlTag:
    def __init__(self, suffix):
        self.suffix = suffix

    def __eq__(self, other):
        return isinstance(other, _OpaqueYamlTag) and other.suffix == self.suffix

    def __hash__(self):
        return hash(self.suffix)


def _mkdocs_yaml_handlers():
    import yaml

    class Loader(yaml.SafeLoader):
        pass

    class Dumper(yaml.SafeDumper):
        pass

    Loader.add_multi_constructor(
        "tag:yaml.org,2002:python/name:",
        lambda loader, suffix, node: _OpaqueYamlTag(suffix),
    )
    Dumper.add_representer(
        _OpaqueYamlTag,
        lambda dumper, data: dumper.represent_scalar(
            f"tag:yaml.org,2002:python/name:{data.suffix}", ""
        ),
    )
    return Loader, Dumper


def _merge_nav_section(existing, generated):
    generated_keys = {key for entry in generated for key in entry}
    preserved = [
        entry
        for entry in existing or []
        if not (isinstance(entry, dict) and generated_keys.issuperset(entry))
    ]
    return generated + preserved


def _update_mkdocs_nav(nav_entries: dict, changelog_entries: dict):
    """Update the Schemata and Schema Change Log sections of mkdocs.yml."""
    import yaml

    Loader, Dumper = _mkdocs_yaml_handlers()

    mkdocs_path = REPO_ROOT / "mkdocs.yml"
    with open(mkdocs_path) as f:
        config = yaml.load(f, Loader=Loader)

    for item in config.get("nav", []):
        if not isinstance(item, dict):
            continue

        if "Schemata" in item:
            for section in item["Schemata"]:
                if not isinstance(section, dict):
                    continue
                for display_name, (docs_subdir, versions) in nav_entries.items():
                    if display_name in section:
                        section[display_name] = _merge_nav_section(
                            section[display_name],
                            [
                                {f"Version {v}": f"{docs_subdir}/{v}.md"}
                                for v in versions
                            ],
                        )

        if "Schema Change Log" in item:
            for section in item["Schema Change Log"]:
                if not isinstance(section, dict):
                    continue
                for display_name, (docs_subdir, versions) in changelog_entries.items():
                    # Match on either the full display name or the short subdir name (e.g. "GWDM")
                    key = display_name if display_name in section else (docs_subdir if docs_subdir in section else None)
                    if key:
                        section[key] = _merge_nav_section(
                            section[key],
                            [
                                {v: f"{docs_subdir}/{v}.change.md"}
                                for v in versions
                            ],
                        )

    with open(mkdocs_path, "w") as f:
        yaml.dump(
            config,
            f,
            Dumper=Dumper,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )


def build_docs():
    nav_entries = {}
    changelog_entries = {}

    for family, (display_name, docs_subdir) in DOC_FAMILIES.items():
        print(f"{family}")
        docs_path = DOCS_DIR / docs_subdir
        docs_path.mkdir(exist_ok=True)

        family_module = importlib.import_module(f"hdr_schemata.models.{family}")

        seen = {}
        for name, cls in inspect.getmembers(family_module, inspect.isclass):
            if not (isinstance(cls, type) and issubclass(cls, BaseModel)):
                continue
            mod = cls.__module__
            if not mod.startswith(f"hdr_schemata.models.{family}.v"):
                continue
            version_dir = mod.split(".")[-1]
            if version_dir not in seen:
                seen[version_dir] = (name, cls)

        versions = []
        structures = {}
        for version_dir in sorted(seen, key=lambda d: _version_sort_key(_version_str(d))):
            _, cls = seen[version_dir]
            version_str = _version_str(version_dir)
            create_markdown(cls, str(docs_path), version_str)
            versions.append(version_str)
            with open(docs_path / f"{version_str}.structure.json") as f:
                structures[version_str] = json.load(f)

        changelog_versions = []
        for i in range(1, len(versions)):
            old_v, new_v = versions[i - 1], versions[i]
            md = generate_change_md(old_v, new_v, structures[old_v], structures[new_v])
            change_path = docs_path / f"{new_v}.change.md"
            with open(change_path, "w") as f:
                f.write(md)
            print(f"  changelog {old_v} -> {new_v}")
            changelog_versions.append(new_v)

        nav_entries[display_name] = (docs_subdir, versions)
        changelog_entries[display_name] = (docs_subdir, changelog_versions)

    _update_mkdocs_nav(nav_entries, changelog_entries)
    print("\nmkdocs.yml nav updated")


if __name__ == "__main__":
    build_docs()
