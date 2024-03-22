from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards


class FormatAndStandards(BaseModel):
    class Config:
        extra = "forbid"

    vocabularyEncodingScheme: Union[
        Optional[CommaSeparatedValues], List[ControlledVocabulary]
    ] = Field(..., **an.vocabularyEncodingScheme.__dict__)
    conformsTo: Union[Optional[CommaSeparatedValues], List[StandardisedDataModels]] = (
        Field(..., **an.vocabularyEncodingScheme.__dict__)
    )
    language: Union[Optional[CommaSeparatedValues], List[Language]] = Field(
        ..., **an.vocabularyEncodingScheme.__dict__
    )
    format: Union[Optional[CommaSeparatedValues], List[Format]] = Field(
        ..., **an.vocabularyEncodingScheme.__dict__
    )
