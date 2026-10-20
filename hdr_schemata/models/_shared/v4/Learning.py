from typing import List, Optional
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.learning


class Learning(BaseModel):
    class Config:
        extra = "forbid"

    tags: Optional[List[OneHundredFiftyCharacters]] = Field(None, **an.tags.__dict__)

    summary: Optional[TwoHundredFiftyFiveCharacters] = Field(None, **an.summary.__dict__)

    content: Optional[RichText] = Field(None, **an.content.__dict__)
