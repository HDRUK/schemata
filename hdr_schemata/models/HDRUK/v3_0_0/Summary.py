from hdr_schemata.models import remove_fields_from_cls
from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .Organisation import Organisation

from .annotations import annotations

an = annotations.summary

class Summary(BaseModel):
    class Config:
        extra = "forbid"

    title: OneHundredFiftyCharacters = Field(
        ..., **an.title.__dict__, json_schema_extra={"guidance": an.title.guidance}
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
    
    alternateIdentifiers: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[ShortDescription]]]
    ] = Field(None, **an.alternateIdentifiers.__dict__)
