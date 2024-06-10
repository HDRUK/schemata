from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .DatasetDescriptor import DatasetDescriptor

from .annotations import annotations

an = annotations.enrichmentAndLinkage


class EnrichmentAndLinkage(BaseModel):
    class Config:
        extra = "forbid"

    derivedFrom: Optional[List[DatasetDescriptor]] = Field(
        None, **an.derivedFrom.__dict__, json_schema_extra={"guidance": an.derivedFrom.guidance}
    )

    isPartOf: Optional[List[DatasetDescriptor]] = Field(
        None, **an.isPartOf.__dict__, json_schema_extra={"guidance": an.isPartOf.guidance}
    )

    linkableDatasets: Optional[List[DatasetDescriptor]] = Field(
        None, **an.linkableDatasets.__dict__, json_schema_extra={"guidance": an.linkableDatasets.guidance}
    )

    similarToDatasets: Optional[List[DatasetDescriptor]] = Field(
        None, **an.similarToDatasets.__dict__, json_schema_extra={"guidance": an.similarToDatasets.guidance}
    )

    investigations: Optional[List[Url]] = Field(
        None, **an.investigations.__dict__, json_schema_extra={"guidance": an.investigations.guidance}
    )
    
    tools: Optional[List[Url]] = Field(
        None, **an.tools.__dict__, json_schema_extra={"guidance": an.tools.guidance}
    )

    publicationAboutDataset: Optional[List[Doi]
    ] = Field(
        None, 
        **an.publicationAboutDataset.__dict__, 
        json_schema_extra={"guidance": an.publicationAboutDataset.guidance}
    )

    publicationUsingDataset: Optional[List[Doi]
    ] = Field(
        None, 
        **an.publicationUsingDataset.__dict__, 
        json_schema_extra={"guidance": an.publicationUsingDataset.guidance}
    )

