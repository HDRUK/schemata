from typing import Optional
from pydantic import RootModel, constr

class CommaSeparatedValues(RootModel):
    root: Optional[constr(pattern=r'([^,]+)')]

class CommaSeparatedValuesV2(RootModel):
    root: Optional[constr(pattern=r'([^,]*)')]