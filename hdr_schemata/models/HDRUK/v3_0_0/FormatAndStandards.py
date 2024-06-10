from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards


class FormatAndStandards(BaseModel):
    class Config:
        extra = "forbid"
        
    vocabularyEncodingScheme: List[ControlledVocabulary] = Field(
        ..., **an.vocabularyEncodingScheme.__dict__
    )

    conformsTo: List[StandardisedDataModels] = Field(
        ..., **an.conformsTo.__dict__
    )

    language: Union[Optional[CommaSeparatedValues], List[Language]] = Field(
        ..., **an.language.__dict__
    )

    format: Union[Optional[CommaSeparatedValues], List[Format]] = Field(
        ..., **an.format.__dict__
    )
