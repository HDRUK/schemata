from typing import Optional
from pydantic import RootModel,constr

class LongAbstractText(RootModel):
    root: Optional[constr(min_length=5, max_length=5000)]


