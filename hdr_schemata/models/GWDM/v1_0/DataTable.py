from typing import Optional, List
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .DataColumn import DataColumn

class DataTable(BaseModel):
    class Config:
        extra = 'forbid'

    name: Optional[constr(min_length=1, max_length=500)] = Field(
        ...,
        description='The name of a table in a dataset.',
        title='Table Name'
    )
    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None,
        description='A description of a table in a dataset.',
        title='Table Description',
    )
    columns: List[DataColumn] = Field(
        ...,
        description='A list of columns contained within a table in a dataset.',
        title='Data Columns',
    )
