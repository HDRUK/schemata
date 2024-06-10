from typing import Optional
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *


class DatasetDescriptor(BaseModel):
    pid: Optional[OneHundredFiftyCharacters] = Field(...)
    title: Optional[OneHundredFiftyCharacters] = Field(...)
    url: Optional[Url] = Field(...)

