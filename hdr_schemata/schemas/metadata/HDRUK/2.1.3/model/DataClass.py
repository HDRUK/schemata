from typing import Optional, List
from pydantic import BaseModel, Field, constr
from definitions import *

from DataElement import DataElement 

class DataClass(BaseModel):
    class Config:
        extra = 'forbid'

    name: Optional[constr(min_length=1, max_length=500)] = Field(
        ..., description='The name of a table in a dataset.', title='Table Name'
    )
    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None,
        description='A description of a table in a dataset.',
        title='Table Description',
    )
    elements: List[DataElement] = Field(
        ...,
        description='A list of data elements contained within a table in a dataset.',
        title='Data Elements',
    )
