from pydantic import BaseModel, Field
from enum import Enum
from typing import Union
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.demographicFrequency.disease


class Disease(BaseModel):
    diseaseCode: Union[str, int] = Field(..., **an.diseaseCode.__dict__)
    diseaseCodeVocabulary: DiseaseCodeEnum = Field(
        ..., **an.diseaseCodeVocabulary.__dict__
    )
    count: int = Field(..., **an.count.__dict__)
