from __future__ import annotations

from typing import Optional

from pydantic import Field, constr

from hdr_schemata.models.GWDM.v2_0.Summary import Summary as Gwdm20Summary

LineSeparatedValues = constr(pattern=r"([^\r\n]+)")


class Summary(Gwdm20Summary):
    funders: Optional[LineSeparatedValues] = Field(
        None,
        title="Funded by",
        description="List of Funders separated by a line break",
        examples=["CRUK", "University of Sussex"],
        json_schema_extra={"guidance": "Put each funder on a new line"},
    )
