from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class Format(BaseModel):
    root: constr(min_length=1)


