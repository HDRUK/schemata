from typing import Optional
from pydantic import RootModel, constr

class AgeRange(RootModel):
    root: Optional[
        constr(
            pattern=r'Not Known|(150|1[0-4][0-9]|[0-9]|[1-8][0-9]|9[0-9])-(150|1[0-4][0-9]|[0-9]|[1-8][0-9]|9[0-9])'
        )
    ]


