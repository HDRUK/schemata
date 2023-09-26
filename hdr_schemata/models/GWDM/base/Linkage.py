from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .DatasetLinkage import DatasetLinkage 

class Linkage(BaseModel):
    class Config:
        extra = 'forbid'

    isGeneratedUsing: Optional[CommaSeparatedValues] = Field(
        None,
        description='',
        title=''
    )

    associatedMedia: Optional[CommaSeparatedValues] = Field(
        None,
        description='',
        title=''
    )

    dataUses: Optional[CommaSeparatedValues] = Field(
        None,
        description='',
        title=''
    )

    isReferenceIn: Optional[CommaSeparatedValues] = Field(
        None,
        description='',
        title=''
    )
    
    tools: Optional[CommaSeparatedValues] = Field(
        None,
        description='tools',
        title='Tools',
    )

    datasetLinkage: Optional[DatasetLinkage] = Field(
        None,
        description='Dataset Linkage copied over from',
        title='Dataset Linkage',
    )
        
    investigations: Optional[CommaSeparatedValues] = Field(
        None,
        title='Investigations'
    )
    
