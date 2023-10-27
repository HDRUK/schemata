from typing import Optional
from pydantic import RootModel, constr

class CommaSeparatedIntegers(RootModel):
    root: Optional[constr(pattern=r'^\d+(,\d+)*$')]


