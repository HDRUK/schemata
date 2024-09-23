from typing import Optional
from pydantic import constr, RootModel

class Url(RootModel):
    root: Optional[constr(pattern=r'^\s*((https?:\/\/)*([a-zA-Z0-9-]+\.?)+[a-zA-Z]{2,}(:\d+)?(\/[^\s]*)?(\n)?)+$')]


