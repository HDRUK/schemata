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

    title: OneHundredFiftyCharacters = Field(..., **an.title.__dict__)

    abstract: AbstractText = Field(..., **an.abstract.__dict__)
    
    dataProvider: Organisation = Field(
        ..., title=an.dataProvider.title, description=an.dataProvider.description
    )

    populationSize: int = Field(..., **an.populationSize.__dict__)

    keywords: Union[Optional[CommaSeparatedValues], List[OneHundredFiftyCharacters]] = (
        Field(..., **an.keywords.__dict__)
    )

    doiName: Optional[Doi] = Field(None, **an.doiName.__dict__)

    contactPoint: EmailAddress = Field(..., **an.contactPoint.__dict__)
    
    alternateIdentifiers: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[ShortDescription]]]
    ] = Field(None, **an.alternateIdentifiers.__dict__)
