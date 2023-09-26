from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

from .Required import Required
from .Summary import Summary
from .Coverage import Coverage
from .Provenance import Provenance
from .Accessibility import Accessibility
from .Linkage import Linkage
from .DataClass import DataClass

class GwdmBaseModel(BaseModel):
    class Config:
        extra = 'forbid'

    required: Required = Field(
        ...,
        description='required metadata needed for the GWDM',
        title='Required'
    )

    summary: Summary = Field(
        ...,
        description='Summary of metadata describing key pieces of information.',
        title='Summary',
    )
    
    coverage: Optional[Coverage] = Field(
        description='Spatial and Temporal coverage',
        title='Coverage',
    )

    provenance: Optional[Provenance] = Field(
        None,
        description='Provenance information',
        title='Provenance',
    )
    
    accessibility: Accessibility = Field(
        ...,
        description='Accessibility information.',
        title='Accessibility',
    )
    
    enrichmentAndLinkage: Optional[EnrichmentAndLinkage] = Field(
        None,
        description='Linkage and enrichment.',
        title='Enrichment and Linkage',
    )
    
    observations: List[Observation] = Field(
        ...,
        description='Obsservations',
        title='Observations',
    )
    structuralMetadata: Optional[List[DataClass]] = Field(
        None,
        description='Descriptions of all tables and data elements that can be included in the dataset',
        title='Structural Metadata',
    )
