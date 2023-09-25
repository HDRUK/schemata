from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class Source(Enum):
    EPR = 'EPR'
    ELECTRONIC_SURVEY = 'ELECTRONIC SURVEY'
    LIMS = 'LIMS'
    OTHER_INFORMATION_SYSTEM = 'OTHER INFORMATION SYSTEM'
    PAPER_BASED = 'PAPER BASED'
    FREETEXT_NLP = 'FREETEXT NLP'
    MACHINE_GENERATED = 'MACHINE GENERATED'
    OTHER = 'OTHER'


