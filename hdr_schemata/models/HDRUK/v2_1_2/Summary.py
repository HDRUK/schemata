from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .Organisation import Organisation

from hdr_schemata.annotations import annotations

an = annotations.HDRUK.v2p1p2.summary


class Summary(BaseModel):
    class Config:
        extra = "forbid"

    title: OneHundredFiftyCharacters = Field(..., **an.title.__dict__)

    abstract: Optional[AbstractText] = Field(..., **an.abstract.__dict__)

    publisher: Organisation = Field(..., **an.publisher.__dict__)

    contactPoint: Optional[EmailAddress] = Field(..., **an.contactPoint.__dict__)

    keywords: Union[Optional[CommaSeparatedValues], List[OneHundredFiftyCharacters]] = (
        Field(..., **an.keywords.__dict__)
    )

    alternateIdentifiers: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[ShortDescription]]]
    ] = Field(None, **an.alternateIdentifiers.__dict__)

    doiName: Optional[Doi] = Field(None, **an.doiName.__dict__)
