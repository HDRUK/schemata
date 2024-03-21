from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.coverage


class Coverage(BaseModel):

    # note: limit these to country codes?
    #      what about regions? surely it's more interesting to know:
    #      scotland:lothian, england:yorkshire, etc.
    spatial: Optional[CommaSeparatedValues] = Field(None, **an.spatial.__dict__)

    # note: limit these instead of arbitrary CommaSeparatedValues
    #      see: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/PhysicalSampleAvailability.py
    # note: this would also be useful to know in a bit more detail, and not always 'sample'
    #      e.g.: <WHAT SAMPLE>::<WHAT MEASURED>::<HOW> ... SERUM::IgG::Abbott
    # note: What about measurements (e.g. serum anti-IgG to SARs-CoV-2)?
    #      What about drug exposures (e.g. vaccine AZ)?
    #      What about medicine given (e.g. diazepam) ?
    #      What about observations (e.g. smoker)?
    physicalSampleAvailability: Optional[CommaSeparatedValues] = Field(
        None, **an.physicalSampleAvailability.__dict__
    )

    # note: missing coverage of the types of people the dataset is covering?
    #      diabetes, cancer, care home residents, smokers, etc. etc.
    #      i.e. not just the 'sample'
    #
    # Could do something OMOP-like:
    # measurements: Optional[CommaSeparatedValues]
    # drugs: Optional[CommaSeparatedValues]
    # observations: Optional[CommaSeparatedValues]

    # note: is this appropriate in this coverage section?
    pathway: Optional[LongDescription] = Field(None, **an.pathway.__dict__)

    # note: May need to update/modify:
    #      https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/Followup.py
    followup: Optional[Followup] = Field(None, **an.followup.__dict__)

    # note: not sure if this is the best way of doing it
    #      ask for age: low, median, high instead?
    #      allowing [0-150] is not useful ...
    typicalAgeRange: Optional[AgeRange] = Field(None, **an.typicalAgeRange.__dict__)
