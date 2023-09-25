from typing import Optional
from pydantic import RootModel

from .ControlledVocabularyEnum import ControlledVocabularyEnum

class ControlledVocabulary(RootModel):
    root: Optional[ControlledVocabularyEnum] = None


