from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .Organisation import Organisation

from .annotations import annotations

an = annotations.summary


class Summary(BaseModel):
    class Config:
        extra = "forbid"

    title: OneHundredFiftyCharacters = Field(..., **an.title.__dict__)

    abstract: Optional[AbstractText] = Field(..., **an.abstract.__dict__)

    publisher: Organisation = Field(
        ..., title=an.publisher.title, description=an.publisher.description
    )

    contactPoint: Optional[EmailAddress] = Field(..., **an.contactPoint.__dict__)

    keywords: Union[Optional[CommaSeparatedValues], List[OneHundredFiftyCharacters]] = (
        Field(..., **an.keywords.__dict__)
    )

    alternateIdentifiers: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[ShortDescription]]]
    ] = Field(None, **an.alternateIdentifiers.__dict__)

    doiName: Optional[Doi] = Field(None, **an.doiName.__dict__)
