from typing import Optional
from pydantic import RootModel, constr


class ICD_0_3(RootModel):
    root: Optional[constr(pattern=r"^[C\d]{3}\.\d{4}\/\d{1,4}$")]
