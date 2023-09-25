from typing import Optional
from pydantic import BaseModel
from .LanguageEnum import LanguageEnum

class Language(BaseModel):
    root: Optional[LanguageEnum] = None


