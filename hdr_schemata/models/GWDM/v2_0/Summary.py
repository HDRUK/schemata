from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

from .Organisation import Organisation

from .annotations import annotations

an = annotations.summary


class Summary(BaseModel):

    title: TwoHundredFiftyFiveCharacters = Field(..., **an.title.__dict__)

    shortTitle: Optional[ShortTitle] = Field(None, **an.shortTitle.__dict__)

    doiName: Optional[Doi] = Field(None, **an.doiName.__dict__)

    abstract: LongAbstractText = Field(..., **an.abstract.__dict__)

    keywords: Optional[CommaSeparatedValues] = Field(None, **an.keywords.__dict__)

    controlledKeywords: Optional[CommaSeparatedValues] = Field(
        None, **an.controlledKeywords.__dict__
    )

    contactPoint: Optional[EmailStr] = Field(None, **an.contactPoint.__dict__)

    datasetType: Optional[DatasetType] = Field(None, **an.datasetType.__dict__)

    description: Optional[LongDescription] = Field(None, **an.description.__dict__)

    publisher: Optional[Organisation] = Field(
        None,
        description=an.publisher.description,
        title=an.publisher.title,
    )

    populationSize: Optional[int] = Field(None, **an.populationSize.__dict__)

    datasetSubType: Optional[DatasetType] = Field(None, **an.datasetSubType.__dict__)

    inPipeline: Optional[Pipeline] = Field("Not available", **an.inPipeline.__dict__)


