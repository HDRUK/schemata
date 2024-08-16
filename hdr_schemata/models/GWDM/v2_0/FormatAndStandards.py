from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards


class FormatAndStandards(BaseModel):
    class Config:
        extra = "forbid"

    vocabularyEncodingSchemes: Optional[CommaSeparatedValues] = Field(
        None, **an.vocabularyEncodingSchemes.__dict__
    )

    conformsTo: Optional[CommaSeparatedValues] = Field(None, **an.conformsTo.__dict__)

    languages: Optional[CommaSeparatedValues] = Field(None, **an.languages.__dict__)

    formats: Optional[CommaSeparatedValues] = Field(None, **an.formats.__dict__)
