from hdr_schemata.models.HDRUK.v2_1_2 import DataClass as BaseDataClass
from typing import Optional, List
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .Column import Column

from .annotations import annotations

an = annotations.dataClass


class DataClass(BaseDataClass):

    columns: List[Column] = Field(..., **an.column.__dict__)