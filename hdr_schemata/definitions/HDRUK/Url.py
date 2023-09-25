from typing import Optional
from pydantic import AnyUrl, RootModel

class Url(RootModel):
    root: Optional[AnyUrl]


