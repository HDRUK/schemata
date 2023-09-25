from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class Periodicity(Enum):
    STATIC = 'STATIC'
    IRREGULAR = 'IRREGULAR'
    CONTINUOUS = 'CONTINUOUS'
    BIENNIAL = 'BIENNIAL'
    ANNUAL = 'ANNUAL'
    BIANNUAL = 'BIANNUAL'
    QUARTERLY = 'QUARTERLY'
    BIMONTHLY = 'BIMONTHLY'
    MONTHLY = 'MONTHLY'
    BIWEEKLY = 'BIWEEKLY'
    WEEKLY = 'WEEKLY'
    SEMIWEEKLY = 'SEMIWEEKLY'
    DAILY = 'DAILY'
    OTHER = 'OTHER'
    NoneType_None = None


