import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
FORM_SCHEMAS = sorted((REPO_ROOT / "docs").glob("*/*.form.json"))


def walk_fields(node):
    if isinstance(node, dict):
        if isinstance(node.get("types"), dict):
            yield node
        for value in node.values():
            yield from walk_fields(value)
    elif isinstance(node, list):
        for value in node:
            yield from walk_fields(value)


def test_form_schemas_exist():
    assert FORM_SCHEMAS, "no generated *.form.json found - run python -m hdr_schemata.build"


@pytest.mark.parametrize("path", FORM_SCHEMAS, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_object_options_are_well_formed_pairs(path):
    malformed = []
    for field in walk_fields(json.loads(path.read_text())):
        types = field["types"]
        options = types.get("options")
        if not isinstance(options, list) or types.get("type") == "nested":
            continue

        members = [option for option in options if option is not None]
        objects = [option for option in members if isinstance(option, dict)]
        if not objects:
            continue

        location = field.get("location", field.get("title", "?"))
        if len(objects) != len(members):
            malformed.append(f"{location}: mixes object and scalar members")
        for option in objects:
            if set(option) != {"value", "label"}:
                malformed.append(f"{location}: object member has keys {sorted(option)}")

    assert malformed == [], (
        f"{path.relative_to(REPO_ROOT)} emits malformed option objects: {malformed}. "
        "Traser's hydration map normalises {value, label} pairs into a flat validation "
        "enum plus enum_titles; a member missing either key, or a list mixing objects "
        "with scalars, breaks that normalisation and reaches schema-to-yup as an object, "
        "which it spreads and throws on."
    )


@pytest.mark.parametrize("path", FORM_SCHEMAS, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_option_titles_align_with_options(path):
    misaligned = []
    for field in walk_fields(json.loads(path.read_text())):
        types = field["types"]
        if "option_titles" not in types:
            continue
        if len(types["option_titles"]) != len(types.get("options", [])):
            misaligned.append(field.get("location", field.get("title", "?")))

    assert misaligned == [], (
        f"{path.relative_to(REPO_ROOT)} has option_titles of a different length to "
        f"options: {misaligned}. Consumers index the two arrays positionally."
    )
