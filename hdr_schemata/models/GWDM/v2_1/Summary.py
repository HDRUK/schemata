from __future__ import annotations

from typing import Optional

from pydantic import Field

from hdr_schemata.definitions.HDRUK import CommaSeparatedValues
from hdr_schemata.models.GWDM.v2_0.Summary import Summary as Gwdm20Summary


class Summary(Gwdm20Summary):
    funders: Optional[CommaSeparatedValues] = Field(
        None,
        title="Funded by",
        description="Comma-separated list of funders for this dataset.",
        examples=["CRUK,University of Sussex"],
        json_schema_extra={"guidance": "Separate each funder with a comma."},
    )
