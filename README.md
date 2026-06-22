# schemata-2

Canonical metadata schema definitions for the HDR UK Gateway platform. Schemas are authored as Pydantic v2 models; JSON Schema files and Markdown documentation are auto-generated from them.

Full documentation: **https://hdruk.github.io/schemata-2/**

## Setup

```bash
pip install -e .              # install package in editable mode
pip install -r requirements.txt  # docs and test dependencies
```

## Commands

```bash
# Run tests
pytest hdr_schemata/tests/

# Regenerate schema.json files and available.json (run before committing model changes)
python hdr_schemata/utils/build.py

# Regenerate docs/ markdown from Pydantic models
python hdr_schemata/utils/create_markdown.py
```

## Docs

```bash
mkdocs serve           # local preview at http://127.0.0.1:8000
mkdocs build --strict  # validate all pages build without errors
mkdocs gh-deploy --force  # deploy to GitHub Pages (master branch; CI does this automatically)
```

## Modifying a schema

The below is a walkthrough of the steps required to make a change to an existing schema, by way of
an example. Other changes will require slightly different steps.

In this example, we wish to modify the type of a field (`accessibility.formatAndStandards.conformsTo`)
in the HDRUK 2.2.1 schema.

### Modify schema files

The schema definition in `hdr_schemata/models/HDRUK/2.2.1/schema.json` is
generated from the contents of `hdr_schemata/models/HDRUK/v2_2_1`, building
upon the contents of previous versions. `v2_1_2` is the "base model" all
current schemas are derived from.

We create a new `FormatAndStandards.py` in the
`v2_2_1` directory, with the boilerplate taken from `v2_1_2/FormatAndStandards.py`. Into this file we import
```python
from hdr_schemata.models.HDRUK.v2_2_0 import (
    FormatAndStandards as BaseFormatAndStandards,
)
```
Note that this is from the previous version, which itself imports from `v2_1_2`. Ensure that the `v2_1_2/__init__.py` correctly exports the class.

Overload the class, using the imported class as base:
```python
class FormatAndStandards(BaseFormatAndStandards):
    conformsTo: Optional[List[StandardisedDataModels]] = Field(
        ..., **an.vocabularyEncodingScheme.__dict__
    )
```

Now import this file into `v2_2_1/Accessibility.py`, and overload the field there with the new type:

```python
class Accessibility(BaseAccessibility):
    access: Access = Field(..., description=an.description, title=an.title)

    formatAndStandards: Optional[FormatAndStandards] = Field(
        None,
        title=an.formatAndStandards.title,
        description=an.formatAndStandards.description,
    )
```

### Regenerate schema JSON and docs

```bash
python hdr_schemata/utils/build.py          # updates schema.json + available.json
python hdr_schemata/utils/create_markdown.py  # updates docs/
```

After merging to `master`, the updated docs are automatically published at `https://hdruk.github.io/schemata-2/`.

See the [full contributing guide](https://hdruk.github.io/schemata-2/contributing/) for more detail on writing new versions, the release workflow, and local doc previews.
