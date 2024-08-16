from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards


class FormatAndStandards(BaseModel):
    class Config:
        extra = "forbid"

    vocabularyEncodingScheme: List[ControlledVocabularyEnum] = Field(
        None,
        **an.vocabularyEncodingScheme.__dict__,
        json_schema_extra={"guidance": an.vocabularyEncodingScheme.guidance}
    )

    conformsTo: List[StandardisedDataModelsEnum] = Field(
        None,
        **an.conformsTo.__dict__,
        json_schema_extra={"guidance": an.conformsTo.guidance}
    )

    language: List[LanguageEnum] = Field(
        None,
        **an.language.__dict__,
        json_schema_extra={"guidance": an.language.guidance}
    )

<<<<<<< HEAD
    format: List[Format] = Field(
        None, **an.format.__dict__, json_schema_extra={"guidance": an.format.guidance}
=======
    format: Union[List[Format], Optional[CommaSeparatedValues]] = Field(
        ..., **an.format.__dict__, json_schema_extra={"guidance": an.format.guidance}
>>>>>>> 5c24292 (debugging from onboarding form)
    )
