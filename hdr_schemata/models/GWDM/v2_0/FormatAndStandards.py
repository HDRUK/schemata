from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards


class FormatAndStandards(BaseModel):
    class Config:
        extra = "forbid"

    vocabularyEncodingSchemes: Optional[CommaSeparatedValuesV2] = Field(
        None, **an.vocabularyEncodingSchemes.__dict__
    )

    conformsTo: Optional[CommaSeparatedValuesV2] = Field(None, **an.conformsTo.__dict__)

    languages: Optional[CommaSeparatedValuesV2] = Field(None, **an.languages.__dict__)

    formats: Optional[CommaSeparatedValuesV2] = Field(None, **an.formats.__dict__)
