from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .DatasetLinkage import DatasetLinkage 

class Linkage(BaseModel):
    class Config:
        extra = 'forbid'

    #note: this is a new field
    #      what are we going to do with it?
    isGeneratedUsing: Optional[CommaSeparatedValues] = Field(
        None,
        description='??',
        title='Is Generated Using'
    )

    #note: may need to be commad separated list of URLs?
    associatedMedia: Optional[CommaSeparatedValues] = Field(
        None,
        description='Any media associated with the Gateway Organisation using a valid URI for the content. This is an opportunity to provide additional context that could be useful for researchers wanting to understand more about the dataset and its relevance to their research question',
        example= "https://popdatasci.swan.ac.uk/centres-of-excellence/sail/,https://www.youtube.com/watch?v=ZK9-Jw3uVkw,https://saildatabank.com/,https://saildatabank.com/about-us/",
        title='Associated Media'
    )

    #note: new field - what are we going to do with it??
    dataUses: Optional[CommaSeparatedValues] = Field(
        None,
        description='??',
        title='Data Uses'
    )

    #note: dont we have this already somewhere else? Linked DOIs?
    isReferenceIn: Optional[CommaSeparatedValues] = Field(
        None,
        description='Rhe keystone paper associated with the dataset. Also include a list of known citations, if available and s\
hould be links to existing resources where the dataset has been used or referenced.',
        title='Is Reference in'
    )

    #note: limit this is comma separated values of URLs?
    tools: Optional[CommaSeparatedValues] = Field(
        None,
        description='URL of any analysis tools or models that have been created for this dataset and are available for further use',
        example="https://conceptlibrary.saildatabank.com/",
        title='Tools',
    )

    datasetLinkage: Optional[DatasetLinkage] = Field(
        None,
        description='Dataset Linkage copied over from',
        title='Dataset Linkage',
    )

    #note: something wrong with this description and/or something needs updating with what this is needed for... 
    investigations: Optional[CommaSeparatedValues] = Field(
        None,
        description='Please provide the keystone paper associated with the dataset.',
        example="https://digital.nhs.uk/services/data-access-request-service-dars/register-of-approved-data-releases",
        title='Investigations'
    )
    
