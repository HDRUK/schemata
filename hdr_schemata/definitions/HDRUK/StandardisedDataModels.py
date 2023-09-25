from typing import Optional
from pydantic import RootModel

from .StandardisedDataModelsEnum import StandardisedDataModelsEnum

class StandardisedDataModels(RootModel):
    root: Optional[StandardisedDataModelsEnum] = None


