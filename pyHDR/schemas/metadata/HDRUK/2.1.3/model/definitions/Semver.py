from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class Semver(BaseModel):
    root: constr(pattern=r'^([0-9]+)\.([0-9]+)\.([0-9]+)$')

    
