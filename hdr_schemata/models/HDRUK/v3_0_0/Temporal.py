from pydantic import Field
from typing import Optional, Union
from datetime import date, datetime
from hdr_schemata.definitions.HDRUK import *
from hdr_schemata.models.HDRUK.v2_1_3.Temporal import Temporal as BaseTemporal
from hdr_schemata.models import remove_fields_from_cls


from .annotations import annotations

an = annotations.provenance.temporal


class Temporal(BaseTemporal):
    publishingFrequency: PeriodicityV2 = Field(..., **an.publishingFrequency.__dict__)

    distributionReleaseDate: Optional[Union[date, datetime]] = Field(
        None, **an.distributionReleaseDate.__dict__
    )

    startDate: Union[date, datetime] = Field(..., **an.startDate.__dict__)
    
    endDate: Optional[Union[date, datetime, EndDateEnum]] = Field(
        None, **an.endDate.__dict__
    )

    timeLag: TimeLagV2 = Field(..., **an.timeLag.__dict__)