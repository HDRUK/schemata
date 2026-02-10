from __future__ import annotations

from typing import Optional, Union, List

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import (
    AbstractText,
    CommaSeparatedValues,
    Doi,
    EmailAddress,
    OneHundredFiftyCharacters,
    ShortDescription,
)
from hdr_schemata.models.HDRUK.v4_0_0.Organisation import Organisation
from hdr_schemata.models.HDRUK.v4_0_0.annotations import annotations

from .LineSeparatedValues import LineSeparatedValues

an = annotations.summary


class Summary(BaseModel):
    class Config:
        extra = "forbid"

    title: OneHundredFiftyCharacters = Field(
        ..., **an.title.__dict__, json_schema_extra={"guidance": an.title.guidance}
    )

    funders: LineSeparatedValues = Field(
        ...,
        title="Funded by",
        description="List of Funders separated by a line break",
        examples=["CRUK", "University of Sussex"],
        json_schema_extra={"guidance": "Put each funder on a new line"},
    )

    abstract: AbstractText = Field(
        ..., **an.abstract.__dict__, json_schema_extra={"guidance": an.abstract.guidance}
    )

    dataCustodian: Organisation = Field(
        ..., title=an.dataCustodian.title, description=an.dataCustodian.description
    )

    populationSize: int = Field(
        ..., **an.populationSize.__dict__, json_schema_extra={"guidance": an.populationSize.guidance}
    )

    keywords: Optional[List[OneHundredFiftyCharacters]] = Field(
        None, **an.keywords.__dict__, json_schema_extra={"guidance": an.keywords.guidance}
    )

    doiName: Optional[Doi] = Field(
        None, **an.doiName.__dict__, json_schema_extra={"guidance": an.doiName.guidance}
    )

    contactPoint: EmailAddress = Field(
        ..., **an.contactPoint.__dict__, json_schema_extra={"guidance": an.contactPoint.guidance}
    )

    datasetAliases: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[ShortDescription]]]
    ] = Field(None, **an.datasetAliases.__dict__)
