from typing import Optional

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import *
from hdr_schemata.definitions.HDRUK.CommaSeparatedValues import CommaSeparatedValuesV2

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
