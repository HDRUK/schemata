from datetime import date, datetime
from typing import Optional, Union

from pydantic import BaseModel, Field

from .Origin import Origin
from .Temporal import Temporal


class RetentionPeriod(BaseModel):
    class Config:
        extra = "forbid"

    startDate: Optional[Union[date, datetime]] = Field(
        None,
        title="Retention Start Date",
        description="Start of the data retention period.",
    )
    endDate: Optional[Union[date, datetime]] = Field(
        None,
        title="Retention End Date",
        description="End of the data retention period.",
    )


class Provenance(BaseModel):
    class Config:
        extra = "forbid"

    origin: Optional[Origin] = Field(None)
    temporal: Temporal = Field(...)
    retentionPeriod: Optional[RetentionPeriod] = Field(
        None,
        title="Retention Period",
        description="Data retention period for the dataset (healthdcatap:retentionPeriod).",
    )
