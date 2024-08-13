from pydantic import BaseModel
from enum import Enum
from typing import Union

class DiseaseCodeVocabulary(Enum):
    ICD10 = 'ICD10'
    SNOMED_CT = 'SNOMED CT'
    MESH = 'MeSH'

class Disease(BaseModel):
    diseaseCode: Union[str, int]
    diseaseCodeVocabulary: DiseaseCodeVocabulary
    count: int
