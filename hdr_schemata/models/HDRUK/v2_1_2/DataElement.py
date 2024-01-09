from typing import Optional
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

class DataElement(BaseModel):
    class Config:
        extra = 'allow'

    name: Name = Field(
        ..., description='The name of a column in a table.', title='Column Name'
    )
    dataType: str = Field(
        ..., description='The data type of values in the column', title='Data Type'
    )
    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None,
        description='A description of a column in a table.',
        title='Column Description',
    )
    sensitive: bool = Field(
        ...,
        description='A True or False value, indicating if the field is sensitive or not',
        title='Sensitive',
    )
