import json
from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import * 

from .Revision import Revision
from .Summary import Summary
from .Documentation import Documentation
from .Coverage import Coverage
from .Provenance import Provenance
from .Accessibility import  Accessibility 
from .EnrichmentAndLinkage import EnrichmentAndLinkage
from .Observations import Observation
from .DataClass import DataClass
from .DataElement import DataElement


class Hdruk212(BaseModel):
    class Config:
        extra = 'forbid'

    identifier: Union[Uuidv4, Optional[Url]] = Field(
        ...,
        description='System dataset identifier',
        examples=[
            [
                '226fb3f1-4471-400a-8c39-2b66d46a39b6',
                'https://web.www.healthdatagateway.org/dataset/226fb3f1-4471-400a-8c39-2b66d46a39b6',
            ]
        ],
        title='Dataset identifier',
    )
    version: Semver = Field(
        ...,
        description='Dataset metadata version',
        examples=['1.1.0'],
        title='Dataset Version',
    )
    revisions: List[Revision] = Field(
        ..., description='Revisions of Dataset metadata', title='Dataset Revisions'
    )
    issued: datetime = Field(
        ..., description='Dataset Metadata Creation Date', title='Creation Date'
    )
    modified: datetime = Field(
        ..., description='Dataset Metadata Creation Date', title='Modification Date'
    )
    
    summary: Summary = Field(
        ...,
        description='Summary metadata must be completed by Data Custodians onboarding metadata into the Innovation Gateway MVP.',
        title='Summary',
    )
    
    documentation: Optional[Documentation] = Field(
        None,
        description='Documentation can include a rich text description of the dataset or links to media such as documents, images, presentations, videos or links to data dictionaries, profiles or dashboards. Organisations are required to confirm that they have permission to distribute any additional media.',
        title='Documentation',
    )
    
    coverage: Optional[Coverage] = Field(
        None,
        description='This information includes attributes for geographical and temporal coverage, cohort details etc. to enable a deeper understanding of the dataset content so that researchers can make decisions about the relevance of the underlying data.',
        title='Coverage',
    )
    
    provenance: Optional[Provenance] = Field(
        None,
        description='Provenance information allows researchers to understand data within the context of its origins and can be an indicator of quality, authenticity and timeliness.',
        title='Provenance',
    )
    accessibility: Accessibility = Field(
        ...,
        description='Accessibility information allows researchers to understand access, usage, limitations, formats, standards and linkage or interoperability with toolsets.',
        title='Accessibility',
    )
    enrichmentAndLinkage: Optional[EnrichmentAndLinkage] = Field(
        None,
        description='This section includes information about related datasets that may have previously been linked, as well as indicating if there is the opportunity to link to other datasets in the future. If a dataset has been enriched and/or derivations, scores and existing tools are available this section allows providers to indicate this to researchers.',
        title='Enrichment and Linkage',
    )
    observations: List[Observation] = Field(
        ...,
        description='Multiple observations about the dataset may be provided and users are expected to provide at least one observation (1..*). We will be supporting the schema.org observation model (https://schema.org/Observation) with default values. Users will be encouraged to provide their own statistical populations as the project progresses. Example: &lt;b&gt; Statistical Population 1 &lt;/b&gt; type: StatisticalPopulation populationType: Persons numConstraints: 0 &lt;b&gt; Statistical Population 2 &lt;/b&gt; type: StatisticalPopulation populationType: Events numConstraints: 0 &lt;b&gt; Statistical Population 3 &lt;/b&gt; type: StatisticalPopulation populationType: Findings numConstraints: 0 typeOf: Observation observedNode: &lt;b&gt; Statistical Population 1 &lt;/b&gt; measuredProperty: count measuredValue: 32937 observationDate: “2017”',
        title='Observations',
    )
    structuralMetadata: Optional[List[DataClass]] = Field(
        None,
        description='Descriptions of all tables and data elements that can be included in the dataset',
        title='Structural Metadata',
    )

    @classmethod
    def save_schema(cls,location='./2.1.2/schema.json'):
        with open(location,'w') as f:
            json.dump(cls.model_json_schema(),f,indent=6)
