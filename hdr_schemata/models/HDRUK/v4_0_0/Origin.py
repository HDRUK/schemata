from hdr_schemata.models.HDRUK.v3_0_0.Origin import Origin as BaseOrigin
from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *
from hdr_schemata.models import remove_fields_from_cls

from .annotations import annotations

an = annotations.provenance.origin


class Origin(BaseOrigin):

    datasetType: List[DatasetTypeV3] = Field(
        ..., **an.datasetType.__dict__, json_schema_extra={"guidance": an.datasetType.guidance}
    )

remove_fields_from_cls(Origin, ["datasetSubType"])