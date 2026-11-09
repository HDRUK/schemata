from pydantic import Field

from hdr_schemata.definitions.HDRUK import *
from hdr_schemata.models.GWDM.v2_0.Required import Required as BaseRequired

from .annotations import annotations

an = annotations.required


class Required(BaseRequired):
    recordType: RecordType = Field(RecordType.DATASET, **an.recordType.__dict__)
