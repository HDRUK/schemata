from typing import Optional
from pydantic import RootModel, constr

class Doi(RootModel):
    root: Optional[constr(pattern=r'^10.\d{4,9}/[-._;()/:a-zA-Z0-9]+$')]


