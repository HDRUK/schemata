from pydantic import BaseModel, RootModel
import pandas as pd
import json
import typing
import enum


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

        value = {
            "name": name,
            "required": field.is_required(),
            "title": field.title,
            "description": field.description,
            "title": field.title,
            "examples": field.examples,
            "type": type_names,
            # "types": _types,
            "is_list": is_list,
            "is_optional": is_optional,
        }

        while hasattr(t, "__args__"):
            t = t.__args__[0]

        if isinstance(t, type) and issubclass(t, BaseModel):
            subItems = []
            get_fields(subItems, t)
            value["subItems"] = subItems

        structure.append(value)


def json_to_markdown(structure, level=2):
    md = ""
    for field in structure:
        name = field.pop("name")
        subItems = field.pop("subItems", None)
        description = field.pop("description")
        examples = field.pop("examples")
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


def traverse_structure(data, form, parent=None):
    for item in data:
        k = item.pop("name")
        if parent:
            k = parent + "." + k
        subItems = item.pop("subItems", None)
        if subItems:
            traverse_structure(subItems, form, parent=k)

        types = item.pop("types")
        info = None
        for t in types:
            try:
                if t and issubclass(t, RootModel):
                    info = t.model_json_schema()
            except:
                ...
            if type(t) == enum.EnumMeta:
                info = {"type": "string", "options": [m.value for m in t]}
        _ = item.pop("type")
        item["types"] = info
        form[k] = item


def create_markdown(Model, path, name):
    structure = []
    get_fields(structure, Model)

    # form = {}
    # traverse_structure(structure, form)
    # print(json.dumps(form, indent=6))

    with open(f"{path}/{name}.structure.json", "w") as f:
        print(json.dumps(structure, indent=6))
        json.dump(structure, f, indent=6)

    md = json_to_markdown(structure)

    with open(f"{path}/{name}.md", "w") as f:
        f.write(md)
    print(f"Done {path}/name")


from hdr_schemata.models.HDRUK import Hdruk212
from hdr_schemata.models.HDRUK import Hdruk213
from hdr_schemata.models.HDRUK import Hdruk220
from hdr_schemata.models.HDRUK import Hdruk221
from hdr_schemata.models.GWDM.v1_1 import Gwdm10
from hdr_schemata.models.GWDM.v1_1 import Gwdm11
from hdr_schemata.models.GWDM.v1_2 import Gwdm12


create_markdown(Hdruk220, "./docs/HDRUK/", "2.2.0")
create_markdown(Hdruk221, "./docs/HDRUK/", "2.2.1")
create_markdown(Hdruk212, "./docs/HDRUK/", "2.1.2")
create_markdown(Hdruk213, "./docs/HDRUK/", "2.1.3")

from hdr_schemata.models.GWDM.v1_1 import Gwdm10
from hdr_schemata.models.GWDM.v1_1 import Gwdm11
from hdr_schemata.models.GWDM.v1_2 import Gwdm12

create_markdown(Gwdm10, "./docs/GWDM/", "1.0")
create_markdown(Gwdm11, "./docs/GWDM/", "1.1")
create_markdown(Gwdm12, "./docs/GWDM/", "1.2")
