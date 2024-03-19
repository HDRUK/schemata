from pydantic import Field
from hdr_schemata.definitions.HDRUK import Periodicity
from hdr_schemata.models.HDRUK.v2_1_2.Temporal import Temporal as BaseTemporal
from pydantic import BaseModel, Field
from hdr_schemata.models import remove_fields_from_cls

from hdr_schemata.annotations import annotations

an = annotations.HDRUK.v2p1p3.provenance.temporal


class Temporal(BaseTemporal):
    publishingFrequency: Periodicity = Field(..., **an.publishingFrequency.__dict__)


remove_fields_from_cls(Temporal, ["accrualPeriodicity"])
