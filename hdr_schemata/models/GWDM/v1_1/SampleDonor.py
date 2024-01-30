from typing import Optional, Union
from datetime import date, datetime
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import CommaSeparatedValues


class SampleDonor(BaseModel):
    id: Optional[constr(min_length=2, max_length=50)] = Field(
        None, title="Donor ID", description="ID of the sample donor"
    )

    sex: Optional[str] = Field(
        None, title="Donor Sex", description="Sex of the sample donor"
    )

    birthDate: Optional[Union[date, datetime]] = Field(
        None, title="Donor birth date", description="Date of birth of the sample donor"
    )

    dataCategories: Optional[CommaSeparatedValues] = Field(
        None,
        title="Donor Data Categories",
        description="Data categories related to the sample donor",
    )
