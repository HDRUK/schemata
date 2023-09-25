from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class EndDateEnum(Enum):
    CONTINUOUS = 'CONTINUOUS'
    NoneType_None = None


