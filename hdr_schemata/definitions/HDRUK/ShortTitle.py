from typing import Optional
from pydantic import RootModel,constr

class ShortTitle(RootModel):
    root: Optional[constr(min_length=2, max_length=100)]


