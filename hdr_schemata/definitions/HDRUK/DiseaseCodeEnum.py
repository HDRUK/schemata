from pydantic import BaseModel
from enum import Enum
from typing import Union

class DiseaseCodeEnum(Enum):
    ICD10 = 'ICD10'
    SNOMED_CT = 'SNOMED CT'
    MESH = 'MeSH'
