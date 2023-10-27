from typing import Optional
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

class DataValue(BaseModel):

    name: Name = Field(
        ...,
        description='Unique value in a column .',
        title='Value Name'
    )
    
    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None,
        description='A description of a unique value in a column.',
        title='Value Description',
    )

    frequency: Optional[int] = Field(
        None,
        description='The frequency of occurrance of a value in a column',
        title='Value Frequency',
    )
    
