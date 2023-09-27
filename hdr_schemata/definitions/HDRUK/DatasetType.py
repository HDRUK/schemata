from typing import Optional
from pydantic import RootModel,constr

#note: contructed as a string of max_length=100
#      in the future we may want to limit this with Enums
class DatasetType(RootModel):
    root: Optional[constr(min_length=2, max_length=100)]


