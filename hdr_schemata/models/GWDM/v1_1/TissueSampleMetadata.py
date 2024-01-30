from typing import Optional, Union, List
from pydantic import BaseModel, Field, constr
from datetime import date, datetime
from .SampleDonor import SampleDonor

from hdr_schemata.definitions.HDRUK import CommaSeparatedValues


class TissueSampleMetadata(BaseModel):
    id: Optional[constr(min_length=2, max_length=50)] = Field(
        None, title="Metadata ID", description="ID of the tissue sample metadata"
    )

    sampleDonor: Optional[SampleDonor] = Field(
        None, title="Sample Donor", description="Information about the sample donor"
    )

    sampleType: Optional[CommaSeparatedValues] = Field(
        None, title="Sample Type", description="Type of the tissue sample"
    )

    storageTemperature: Optional[str] = Field(
        None,
        title="Storage Temperature",
        description="Storage temperature of the tissue sample",
    )

    creationDate: Optional[Union[date, datetime]] = Field(
        None,
        title="Creation Date",
        description="Date when the tissue sample metadata was created",
    )

    AnatomicalSiteOntologyCode: Optional[CommaSeparatedValues] = Field(
        None,
        title="Anatomical Site Ontology Code",
        description="Ontology code for the anatomical site",
    )
    AnatomicalSiteOntologyDescription: Optional[CommaSeparatedValues] = Field(
        None,
        title="Anatomical Site Ontology Description",
        description="Ontology description for the anatomical site",
    )

    AnatomicalSiteFreeText: Optional[CommaSeparatedValues] = Field(
        None,
        title="Anatomical Site Free Text",
        description="Free text describing the anatomical site",
    )

    sampleContentDiagnosis: Optional[CommaSeparatedValues] = Field(
        None,
        title="Sample Content Diagnosis",
        description="Diagnosis related to the sample content",
    )

    useReCommaSeparatedValuesictions: Optional[CommaSeparatedValues] = Field(
        None,
        title="Use Restrictions",
        description="Restrictions on the use of the tissue sample",
    )
