from typing import Optional
from pydantic import RootModel, EmailStr

class EmailAddress(RootModel):
    root: Optional[EmailStr]


