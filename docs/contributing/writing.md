# Writing a schema

Schemas are defined as [Pydantic v2](https://docs.pydantic.dev/latest/) `BaseModel` classes. Each schema version lives in its own `vX_Y_Z/` directory and **inherits from the previous version**, overriding only the fields that change.

## Inheritance pattern

`v2_1_2` is the root base for all HDRUK schemas. Every later version imports the previous version's top-level class and subclasses it:

```python
# hdr_schemata/models/HDRUK/v2_2_1/__init__.py

from hdr_schemata.models.HDRUK.v2_2_0 import Hdruk220
from pydantic import Field
from typing import Optional, List

from .Provenance import Provenance
from .annotations import annotations as an


class Hdruk221(Hdruk220):

    provenance: Optional[Provenance] = Field(
        None, description=an.provenance.description, title=an.provenance.title
    )
```

Nested model classes follow the same pattern — import the base from the previous version, subclass it, override only what changes:

```python
# hdr_schemata/models/HDRUK/v2_2_1/Provenance.py

from hdr_schemata.models.HDRUK.v2_2_0 import Provenance as BaseProvenance
from pydantic import Field
from typing import Optional
from .Origin import Origin
from .annotations import annotations

an = annotations.provenance


class Provenance(BaseProvenance):

    origin: Optional[Origin] = Field(
        None, description=an.origin.description, title=an.origin.title
    )
```

## Step-by-step: adding a new version

### 1. Create the version directory

```
hdr_schemata/models/HDRUK/vX_Y_Z/
```

Inside it you need at minimum:

- `__init__.py` — defines the top-level model class, imports sub-models
- Any sub-model files that change from the previous version
- `annotations/` — if you're adding new field annotations for this version

Only create files for things that actually change. Unchanged sub-models are inherited automatically.

### 2. Write the top-level model class

```python
# hdr_schemata/models/HDRUK/vX_Y_Z/__init__.py

import json
from hdr_schemata.models.HDRUK.vW_X_Y import HdrukWXY  # previous version

from .ChangedSection import ChangedSection
from .annotations import annotations as an


class HdrukXYZ(HdrukWXY):

    changedSection: ChangedSection = Field(
        ..., description=an.changedSection.description, title=an.changedSection.title
    )

    @classmethod
    def save_schema(cls, location="./X.Y.Z/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
```

### 3. Use field annotations

Field metadata (titles and descriptions) is stored in `annotations/` YAML files and loaded as attribute objects. Use `an.<field>.title` and `an.<field>.description` rather than hardcoding strings:

```python
from .annotations import annotations as an

myField: str = Field(..., title=an.myField.title, description=an.myField.description)
```

If you're adding a completely new field with no existing annotation, you can inline the strings directly — then consider adding an annotation entry for consistency.

### 4. Register the version in `__init__.py`

Add an import to the family's `__init__.py` so `build.py` picks it up:

```python
# hdr_schemata/models/HDRUK/__init__.py

from .v2_1_2 import Hdruk212
from .v2_1_3 import Hdruk213
# ... existing versions ...
from .vX_Y_Z import HdrukXYZ   # add this line
```

`build.py` discovers versions by inspecting classes exported from the family `__init__.py` — anything not imported here will be invisible to the build.

### 5. Add a test

Create or update a test in `hdr_schemata/tests/test_hdruk.py` (or the relevant family test file). At minimum, validate that an example document passes and an invalid one fails:

```python
class TestHdrukXYZ:
    def test_valid(self):
        with open("hdr_schemata/examples/HDRUK/vX_Y_Z/valid.json") as f:
            HdrukXYZ(**json.load(f))

    def test_invalid(self):
        with pytest.raises(ValidationError):
            HdrukXYZ(requiredField=None)
```

Run the tests before opening a PR:

```bash
pytest hdr_schemata/tests/test_hdruk.py
```

## Removing or excluding fields (Pydantic v2 workaround)

Pydantic v2 does not support `exclude` in model inheritance. Two helpers in `hdr_schemata/models/__init__.py` work around this:

```python
from hdr_schemata.models import filter_fields_in_cls, remove_fields_from_cls

# Keep only these fields (used by SchemaOrg family)
filter_fields_in_cls(MyModel, ["fieldA", "fieldB"])

# Remove specific fields entirely
remove_fields_from_cls(MyModel, ["fieldToRemove"])
```

Both call `model_rebuild(force=True)` internally — call them after the class is defined, not inside it.

## GWDM schemas

The GWDM family follows the same directory and inheritance conventions. The root base is `v1_0`. Version directories are named `v1_0`, `v1_1`, `v2_0`, `v3_0` etc. (no patch component for minor versions). Registration is in `hdr_schemata/models/GWDM/__init__.py`.
