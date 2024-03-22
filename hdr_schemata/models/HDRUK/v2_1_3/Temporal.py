from pydantic import Field
from hdr_schemata.definitions.HDRUK import Periodicity
from hdr_schemata.models.HDRUK.v2_1_2.Temporal import Temporal as BaseTemporal
from pydantic import Field
from hdr_schemata.models import remove_fields_from_cls


from .annotations import annotations

an = annotations.provenance.temporal


class Temporal(BaseTemporal):
    publishingFrequency: Periodicity = Field(..., **an.publishingFrequency.__dict__)


remove_fields_from_cls(Temporal, ["accrualPeriodicity"])
