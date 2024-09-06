from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class MemberOf(Enum):
    HUB = 'HUB'
    ALLIANCE = 'ALLIANCE'
    OTHER = 'OTHER'
    NCS = 'NCS'

class MemberOfV2(Enum):
    HUB = 'Hub'
    ALLIANCE = 'Alliance'
    OTHER = 'Other'
    NCS = 'NCS'

