from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class PhysicalSampleAvailability(Enum):
    NOT_AVAILABLE = 'NOT AVAILABLE'
    BONE_MARROW = 'BONE MARROW'
    CANCER_CELL_LINES = 'CANCER CELL LINES'
    CORE_BIOPSY = 'CORE BIOPSY'
    CDNA_OR_MRNA = 'CDNA OR MRNA'
    DNA = 'DNA'
    FAECES = 'FAECES'
    IMMORTALIZED_CELL_LINES = 'IMMORTALIZED CELL LINES'
    MICRORNA = 'MICRORNA'
    PERIPHERAL_BLOOD_CELLS = 'PERIPHERAL BLOOD CELLS'
    PLASMA = 'PLASMA'
    PM_TISSUE = 'PM TISSUE'
    PRIMARY_CELLS = 'PRIMARY CELLS'
    RNA = 'RNA'
    SALIVA = 'SALIVA'
    SERUM = 'SERUM'
    SWABS = 'SWABS'
    TISSUE = 'TISSUE'
    URINE = 'URINE'
    WHOLE_BLOOD = 'WHOLE BLOOD'
    AVAILABILITY_TO_BE_CONFIRMED = 'AVAILABILITY TO BE CONFIRMED'
    OTHER = 'OTHER'


