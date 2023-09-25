from typing import Optional, Union, List
from pydantic import BaseModel, Field
from definitions import *

class EnrichmentAndLinkage(BaseModel):
    class Config:
        extra = 'forbid'

    qualifiedRelation: Optional[
        Union[
            Optional[CommaSeparatedValues],
            List[Union[Optional[Url], OneHundredFiftyCharacters]],
        ]
    ] = Field(
        None,
        description='If applicable, please provide the DOI of other datasets that have previously been linked to this dataset and their availability. If no DOI is available, please provide the title of the datasets that can be linked, where possible using the same title of a dataset previously onboarded to the HOP. Note: If all the datasets from Gateway organisation can be linked please indicate “ALL” and the onboarding portal will automate linkage across the datasets submitted.',
        title='Linked Datasets',
    )
    derivation: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[AbstractText]]]
    ] = Field(
        None,
        description='Indicate if derived datasets or predefined extracts are available and the type of derivation available. Notes. Single or multiple dimensions can be provided as a derived extract alongside the dataset.',
        title='Derivations',
    )
    tools: Optional[Union[Optional[CommaSeparatedValues], List[Optional[Url]]]] = Field(
        None,
        description='Please provide the URL of any analysis tools or models that have been created for this dataset and are available for further use. Multiple tools may be provided. Note: We encourage users to adopt a model along the lines of https://www.ga4gh.org/news/tool-registry-service-api-enabling-an-interoperable-library-of-genomics-analysis-tools/',
        title='Tools',
    )
