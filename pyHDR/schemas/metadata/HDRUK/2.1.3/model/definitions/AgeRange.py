from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class AgeRange(BaseModel):
    root: Optional[
        constr(
            pattern=r'Not Known|(150|1[0-4][0-9]|[0-9]|[1-8][0-9]|9[0-9])-(150|1[0-4][0-9]|[0-9]|[1-8][0-9]|9[0-9])'
        )
    ]


