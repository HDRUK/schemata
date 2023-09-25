from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class DeliveryLeadTime(Enum):
    LESS_1_WEEK = 'LESS 1 WEEK'
    field_1_2_WEEKS = '1-2 WEEKS'
    field_2_4_WEEKS = '2-4 WEEKS'
    field_1_2_MONTHS = '1-2 MONTHS'
    field_2_6_MONTHS = '2-6 MONTHS'
    MORE_6_MONTHS = 'MORE 6 MONTHS'
    VARIABLE = 'VARIABLE'
    NOT_APPLICABLE = 'NOT APPLICABLE'
    OTHER = 'OTHER'
    NoneType_None = None


