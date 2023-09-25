from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class Followup(Enum):
    field_0___6_MONTHS = '0 - 6 MONTHS'
    field_6___12_MONTHS = '6 - 12 MONTHS'
    field_1___10_YEARS = '1 - 10 YEARS'
    field__10_YEARS = '> 10 YEARS'
    UNKNOWN = 'UNKNOWN'
    CONTINUOUS = 'CONTINUOUS'
    OTHER = 'OTHER'
    NoneType_None = None


