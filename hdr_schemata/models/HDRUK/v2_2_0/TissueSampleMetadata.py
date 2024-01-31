from typing import Optional, Union
from pydantic import BaseModel, Field
from datetime import date, datetime

from hdr_schemata.definitions.HDRUK import ICD_0_3


class TissueSampleMetadata(BaseModel):
    creationDate: Optional[Union[date, datetime]] = Field(
        None,
        title="Creation Date",
        description="Date when the tissue sample metadata was created",
    )

    AnatomicalSiteOntologyCode: Optional[ICD_0_3] = Field(
        None,
        title="Anatomical Site Ontology Code",
        description="Ontology code for the anatomical site, this code must match an ICD-0-3 format",
    )
