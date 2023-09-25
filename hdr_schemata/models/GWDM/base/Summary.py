from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

from .Publisher import Publisher

class Summary(BaseModel):

    title: TwoHundredFiftyFiveCharacters = Field(
        ...,
        title='Title')

    shortTitle: Optional[ShortTitle] = Field(
        ...,
        title='Shorttitle'
    )

    doiName: Optional[Doi] = Field(
        ...,
        title='Doiname'
    )
    
    abstract: LongAbstractText = Field(
        ...,
        title='Abstract'
    )
    
    keywords: Optional[CommaSeparatedValues] = Field(
        ...,
        title='Keywords'
    )

    controlledKeywords: Optional[CommaSeparatedValues] = Field(
        ...,
        title='Controlled Keywords'
    )

    contactPoint: Optional[EmailStr] = Field(
        ...,
        title='Contact Point'
    )

    datasetType: Optional[DatasetType] = Field(
        ...,
        title='Dataset type'
    )
    
    description: Optional[LongDescription] = Field(
        ...,
        title='Description'
    )
    
    publisher: Optional[Publisher] = Field(
        ...,
        title='Publisher',
    )

