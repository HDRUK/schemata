from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

from .Publisher import Publisher

from hdr_schemata.annotations import annotations

an = annotations.GWDM.v1p0.summary


class Summary(BaseModel):

    title: TwoHundredFiftyFiveCharacters = Field(..., **an.title.__dict__)

    shortTitle: Optional[ShortTitle] = Field(..., **an.shortTitle.__dict__)

    doiName: Optional[Doi] = Field(..., **an.doiName.__dict__)

    abstract: LongAbstractText = Field(..., **an.abstract.__dict__)

    keywords: Optional[CommaSeparatedValues] = Field(..., **an.keywords.__dict__)

    # note: do we want to limit these values by Enums?
    controlledKeywords: Optional[CommaSeparatedValues] = Field(
        ..., **an.controlledKeywords.__dict__
    )

    contactPoint: Optional[EmailStr] = Field(..., **an.contactPoint.__dict__)

    # note: new addition added by Damon.. may need to revisit what this should be?
    #      should be Enums?
    datasetType: Optional[DatasetType] = Field(..., **an.datasetType.__dict__)

    description: Optional[LongDescription] = Field(..., **an.description.__dict__)

    publisher: Optional[Publisher] = Field(..., **an.publisher.__dict__)
