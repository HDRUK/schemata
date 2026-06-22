from typing import List, Optional

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import CommaSeparatedValues
from hdr_schemata.models.GWDM.v2_0.annotations import annotations as v20_an

an = v20_an.accessibility.formatAndStandards


class FormatAndStandards(BaseModel):
    class Config:
        extra = "forbid"

    vocabularyEncodingSchemes: Optional[CommaSeparatedValues] = Field(
        None, **an.vocabularyEncodingSchemes.__dict__
    )
    conformsTo: Optional[CommaSeparatedValues] = Field(None, **an.conformsTo.__dict__)
    languages: Optional[CommaSeparatedValues] = Field(None, **an.languages.__dict__)
    formats: Optional[List[str]] = Field(
        None,
        title=an.formats.title,
        description=an.formats.description,
    )
