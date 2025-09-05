from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.coverage


class Coverage(BaseModel):

    spatial: Optional[CommaSeparatedValuesV2] = Field(None, **an.spatial.__dict__)

    pathway: Optional[LongDescription] = Field(None, **an.pathway.__dict__)

    followUp: Optional[FollowupV2] = Field(None, **an.followUp.__dict__)

    typicalAgeRange: Optional[AgeRange] = Field(None, **an.typicalAgeRange.__dict__)

    datasetCompleteness: Optional[Url] = (
        Field(None, **an.datasetCompleteness.__dict__)
    )
