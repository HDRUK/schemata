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

    origin: Optional[Origin] = Field(
        None,
        title="Origin",
        description="Information about how and why the data was originally collected.",
    )

    temporal: Temporal = Field(
        ...,
        title="Temporal",
        description="Temporal coverage and publishing frequency of the dataset.",
    )

    retentionPeriod: Optional[RetentionPeriod] = Field(
        None,
        title="Retention Period",
        description="Period for which the dataset (or records within it) is retained (healthdcatap:retentionPeriod). Provide start and/or end dates to indicate when data will be deleted or archived.",
    )
