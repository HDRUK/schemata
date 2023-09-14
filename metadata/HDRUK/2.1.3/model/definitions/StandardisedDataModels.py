from typing import Optional
from pydantic import BaseModel

from .StandardisedDataModelsEnum import StandardisedDataModelsEnum

class StandardisedDataModels(BaseModel):
    root: Optional[StandardisedDataModelsEnum] = None


