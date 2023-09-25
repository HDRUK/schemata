from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from .ControlledVocabularyEnum import ControlledVocabularyEnum

class ControlledVocabulary(BaseModel):
    root: Optional[ControlledVocabularyEnum] = None


