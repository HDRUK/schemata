from typing import Optional, Union, List
from pydantic import BaseModel, Field, constr
from datetime import date, datetime
from .SampleDonor import SampleDonor

from hdr_schemata.definitions.HDRUK import CommaSeparatedValues


from .annotations import annotations

an = annotations.tissuesSampleCollection.tissueSampleMetadata


class TissueSampleMetadata(BaseModel):
    id: Optional[constr(min_length=2, max_length=50)] = Field(None, **an.id.__dict__)

    sampleDonor: Optional[SampleDonor] = Field(
        None, title=an.sampleDonor.title, description=an.sampleDonor.description
    )

    sampleType: Optional[CommaSeparatedValues] = Field(None, **an.sampleType.__dict__)

    storageTemperature: Optional[str] = Field(None, **an.storageTemperature.__dict__)

    creationDate: Optional[Union[date, datetime]] = Field(
        None, **an.creationDate.__dict__
    )

    anatomicalSiteOntologyCode: Optional[CommaSeparatedValues] = Field(
        None, **an.anatomicalSiteOntologyCode.__dict__
    )

    anatomicalSiteOntologyDescription: Optional[CommaSeparatedValues] = Field(
        None, **an.anatomicalSiteOntologyDescription.__dict__
    )

    anatomicalSiteFreeText: Optional[CommaSeparatedValues] = Field(
        None, **an.anatomicalSiteFreeText.__dict__
    )

    sampleContentDiagnosis: Optional[CommaSeparatedValues] = Field(
        None, **an.sampleContentDiagnosis.__dict__
    )

    useRestrictions: Optional[CommaSeparatedValues] = Field(
        None, **an.useRestrictions.__dict__
    )
