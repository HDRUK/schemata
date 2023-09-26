from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

class DatasetLinkage(BaseModel):
    class Config:
        extra = 'forbid'
        
    derivation: Optional[CommaSeparatedValues] = Field(
        None,
        description='Derivations.',
        title='Derivations',
    )

    isPartOf: Optional[CommaSeparatedValues] = Field(
        None,
        description='',
        title='Is PartOf',
    )

    isMemberOf: Optional[CommaSeparatedValues] = Field(
        None,
        description='',
        title='Is PartOf',
    )

    qualifiedRelation: Optional[CommaSeparatedValues] = Field(
        None,
        description='.',
        title='Linked Datasets',
    )


    investigations: Optional[CommaSeparatedValues] = Field(
        None,
        title='Investigations'
    )
    
