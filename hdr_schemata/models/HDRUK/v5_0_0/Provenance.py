from datetime import date, datetime
from typing import Optional, Union

from pydantic import BaseModel, Field

from hdr_schemata.models.HDRUK.v4_0_0.Provenance import Provenance as Provenance400


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


class Provenance(Provenance400):

    retentionPeriod: Optional[RetentionPeriod] = Field(
        None,
        title="Retention Period",
        description="Period for which the dataset (or records within it) is retained (healthdcatap:retentionPeriod). Provide start and/or end dates to indicate when data will be deleted or archived.",
    )
