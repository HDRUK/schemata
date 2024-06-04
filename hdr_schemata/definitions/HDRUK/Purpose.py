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

class PurposeV2(Enum):
    RESEARCH_COHORT = 'Research cohort'
    STUDY = 'Study'
    DISEASE_REGISTRY = 'Disease registry'
    TRIAL = 'Trial'
    CARE = 'Care'
    AUDIT = 'Audit'
    ADMINISTRATIVE = 'Administrative'
    FINANCIAL = 'Financial'
    STATUATORY = 'Statuatory'
    OTHER = 'Other'
    NoneType_None = None
