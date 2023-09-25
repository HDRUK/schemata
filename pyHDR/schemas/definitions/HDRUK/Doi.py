from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class Doi(BaseModel):
    root: Optional[constr(pattern=r'^10.\d{4,9}/[-._;()/:a-zA-Z0-9]+$')]


