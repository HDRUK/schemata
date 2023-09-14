from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class Isocountrycode(BaseModel):
    root: constr(pattern=r'^[A-Z]{2}(-[A-Z]{2,3})?$')


