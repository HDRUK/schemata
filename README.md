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

# Regenerate everything: schema.json files, available.json, docs/ and the mkdocs nav
python -m hdr_schemata.build

# Verify the committed output matches the models, without writing anything
python -m hdr_schemata.build --check
```

## Regenerating schemas and docs

**If you add or modify a schema, you must run `python -m hdr_schemata.build` and commit
the result.** This is a manual step. One command produces every derived artefact:

| Output | Contents |
|--------|----------|
| `hdr_schemata/models/{family}/{version}/schema.json` | the published JSON Schema |
| `available.json` | the list of families and versions |
| `docs/{family}/{version}.md` | human-readable field reference |
| `docs/{family}/{version}.form.json` | form schema consumed by the Gateway UI |
| `docs/{family}/{version}.structure.json` | structural definition |
| `docs/{family}/{version}.change.md` | generated diff against the previous version |
| `mkdocs.yml` | the `nav` entries for the above |

Versions are discovered from each family's `__init__.py`, so registering your new class
there is what makes it build.

CI runs `python -m hdr_schemata.build --check` and fails with a list of stale files if
the committed output does not match the models.

> **Requires Python 3.11 with `pydantic==2.4.2`** (the pin in `setup.py`). The generated
> markdown and `form.json` depend on the interpreter's type-annotation reprs: on 3.9 the
> generator drops whole field blocks from `form.json` and renders `typing.List[...]`
> instead of `List`. Building on another version will produce a spurious diff that CI
> then rejects.

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
python -m hdr_schemata.build
```

After merging to `master`, the updated docs are automatically published at `https://hdruk.github.io/schemata-2/`.

See the [full contributing guide](https://hdruk.github.io/schemata-2/contributing/) for more detail on writing new versions, the release workflow, and local doc previews.
