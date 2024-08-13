from pydantic import BaseModel
from enum import Enum

class GenderBin(Enum):
    MALE = 'male'
    FEMALE = 'female'

class GenderAssignedAtBirth(BaseModel):
    bin: GenderBin
    count: int
