from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

class DatasetLinkage(BaseModel):
    class Config:
        extra = 'forbid'
        
    isDerivedFrom: Optional[CommaSeparatedValues] = Field(
        None,
        description="Indicate if derived datasets or predefined extracts are available and the type of derivation available. Notes. Single or multiple dimensions can be provided as a derived extract alongside the dataset",
        example="Data will be minimised as appropriate relative to the data access application",
        title='Derivations',
    )

    #note: this could be greatly improved - link with DataCollections or other Dataset objects?
    isPartOf: Optional[CommaSeparatedValues] = Field(
        None,
        description='If the dataset is part of a group or family',
        example="UKCRC Tissue Directory and Coordination Centre",
        title='Is PartOf',
    )

    #note: why was this included? Need to ask Damon as it's an 'extra'
    isMemberOf: Optional[CommaSeparatedValues] = Field(
        None,
        description='Dataset is a member of XXX(?)',
        title='Is MemberOf',
    )

    #note: current data is nonsensical...
    #      make better use out of this my linking to urls or gatewayIDs of other datasets?
    linkedDatasets: Optional[CommaSeparatedValues] = Field(
        None,
        description='Links to other datasets.',
        example="Yes. To any SAIL dataset & reference data.,ALL",
        title='Linked Datasets',
    )    
