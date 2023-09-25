from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class Setting(Enum):
    CLINIC = 'CLINIC'
    PRIMARY_CARE = 'PRIMARY CARE'
    ACCIDENT_AND_EMERGENCY = 'ACCIDENT AND EMERGENCY'
    OUTPATIENTS = 'OUTPATIENTS'
    IN_PATIENTS = 'IN-PATIENTS'
    SERVICES = 'SERVICES'
    COMMUNITY = 'COMMUNITY'
    HOME = 'HOME'
    PRIVATE = 'PRIVATE'
    PHARMACY = 'PHARMACY'
    SOCIAL_CARE = 'SOCIAL CARE'
    LOCAL_AUTHORITY = 'LOCAL AUTHORITY'
    NATIONAL_GOVERNMENT = 'NATIONAL GOVERNMENT'
    OTHER = 'OTHER'


