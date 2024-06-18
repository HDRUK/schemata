New collection of schemas for Enhanced Gateway


## Modifying a schema

The below is a walkthrough of the steps required to make a change to an existing schema, by way of
an example. Other changes will require slightly different steps.

In this example, we wish to modify the type of a field (`accessibility.formatAndStandards.conformsTo`) 
in the HDRUK 2.2.1 schema.

### Modify schema files

The schema definition in `hdr_schemata/models/HDRUK/2.2.1/schema.json` is 
generated from the contents of `hdr_schemata/models/HDRUK/v2_2_1`, building 
upon the contents of previous versions. `v2_1_2 is the "base model" all
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

The changes to the schema are now ready to process.

### Create schema json

Run `python create_json_schema.py`. This will modify the contents of `hdr_schemata/models/HDRUK/2.2.1/schema.json` as appropriate. You may need to install the repo as a local package:
```bash
pip install -e .
```

### Update docs

Finally, update the Markdown docs with:
```bash
python hdr_schemata/utils/create_markdown.py
```
to generate the Markdown in `docs/`. After merging, this will be available at `https://hdruk.github.io/schemata-2/`.
