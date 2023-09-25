from typing import Optional
from pydantic import BaseModel,constr

class AbstractText(BaseModel):
    root: Optional[constr(min_length=5, max_length=500)]


