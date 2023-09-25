from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class Purpose(Enum):
    STUDY = 'STUDY'
    DISEASE_REGISTRY = 'DISEASE REGISTRY'
    TRIAL = 'TRIAL'
    CARE = 'CARE'
    AUDIT = 'AUDIT'
    ADMINISTRATIVE = 'ADMINISTRATIVE'
    FINANCIAL = 'FINANCIAL'
    STATUTORY = 'STATUTORY'
    OTHER = 'OTHER'
    NoneType_None = None


