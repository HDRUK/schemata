from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class StandardisedDataModelsEnum(Enum):
    HL7_FHIR = 'HL7 FHIR'
    HL7_V2 = 'HL7 V2'
    HL7_CDA = 'HL7 CDA'
    HL7_CCOW = 'HL7 CCOW'
    LOINC = 'LOINC'
    DICOM = 'DICOM'
    I2B2 = 'I2B2'
    IHE = 'IHE'
    OMOP = 'OMOP'
    OPENEHR = 'OPENEHR'
    SENTINEL = 'SENTINEL'
    PCORNET = 'PCORNET'
    CDISC = 'CDISC'
    NHS_DATA_DICTIONARY = 'NHS DATA DICTIONARY'
    NHS_SCOTLAND_DATA_DICTIONARY = 'NHS SCOTLAND DATA DICTIONARY'
    NHS_WALES_DATA_DICTIONARY = 'NHS WALES DATA DICTIONARY'
    LOCAL = 'LOCAL'
    OTHER = 'OTHER'


