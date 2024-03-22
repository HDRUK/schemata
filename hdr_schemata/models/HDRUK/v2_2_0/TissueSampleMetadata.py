from typing import Optional, Union
from pydantic import BaseModel, Field
from datetime import date, datetime

from hdr_schemata.definitions.HDRUK import ICD_0_3


from .annotations import annotations

an = annotations.tissuesSampleCollection.tissueSampleMetadata


class TissueSampleMetadata(BaseModel):
    creationDate: Optional[Union[date, datetime]] = Field(
        None, **an.creationDate.__dict__
    )

    AnatomicalSiteOntologyCode: Optional[ICD_0_3] = Field(
        None, **an.AnatomicalSiteOntologyCode.__dict__
    )
