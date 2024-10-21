from typing import Optional
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.datasetDescriptor

class DatasetDescriptor(BaseModel):
    pid: Optional[OneHundredFiftyCharacters] = Field(None, **an.pid.__dict__)
    title: Optional[OneHundredFiftyCharacters] = Field(None, **an.title.__dict__)
    url: Optional[Url] = Field(None, **an.url.__dict__)

