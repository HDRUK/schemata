from typing import Optional
from pydantic import RootModel
from .LanguageEnum import LanguageEnum

class Language(RootModel):
    root: Optional[LanguageEnum] = None


