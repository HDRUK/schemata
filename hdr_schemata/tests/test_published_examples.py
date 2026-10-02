import json
from pathlib import Path

import pytest

PACKAGE_DIR = Path(__file__).parent.parent
EXAMPLES_DIR = PACKAGE_DIR / "examples"
DOCS_DIR = PACKAGE_DIR.parent / "docs"


def _documented_examples() -> list:
    return [
        (example.parent.parent.name, example.parent.name)
        for example in sorted(EXAMPLES_DIR.glob("*/*/example.json"))
        if (DOCS_DIR / example.parent.parent.name / f"{example.parent.name}.structure.json").is_file()
    ]


def _load(path: Path):
    with open(path) as f:
        return json.load(f)


def test_gateway_schema_version_is_published():
    assert ("HDRUK", "4.1.0") in _documented_examples()


@pytest.mark.parametrize("family,version", _documented_examples())
def test_published_example_is_the_validated_example(family, version):
    published = DOCS_DIR / family / f"{version}.example.json"

    assert published.is_file(), f"docs/{family}/{version}.example.json is missing"
    assert _load(published) == _load(EXAMPLES_DIR / family / version / "example.json")


@pytest.mark.parametrize("family,version", _documented_examples())
def test_published_template_has_every_top_level_field(family, version):
    published = DOCS_DIR / family / f"{version}.template.json"
    structure = _load(DOCS_DIR / family / f"{version}.structure.json")

    assert published.is_file(), f"docs/{family}/{version}.template.json is missing"
    assert list(_load(published)) == [item["name"] for item in structure]
