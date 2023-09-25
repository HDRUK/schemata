from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class Description(BaseModel):
    root: Optional[constr(min_length=2, max_length=10000)]


