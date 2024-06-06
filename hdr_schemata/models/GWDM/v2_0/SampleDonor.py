from typing import Optional, Union
from datetime import date, datetime
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import CommaSeparatedValues


from .annotations import annotations

an = annotations.tissuesSampleCollection.tissueSampleMetadata.sampleDonor


class SampleDonor(BaseModel):
    id: Optional[constr(min_length=2, max_length=50)] = Field(None, **an.id.__dict__)

    sex: Optional[str] = Field(None, **an.sex.__dict__)

    birthDate: Optional[Union[date, datetime]] = Field(None, **an.birthDate.__dict__)

    dataCategories: Optional[CommaSeparatedValues] = Field(
        None, **an.dataCategories.__dict__
    )
