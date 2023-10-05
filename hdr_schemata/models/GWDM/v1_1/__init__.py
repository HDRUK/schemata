from hdr_schemata.models.GWDM import Gwdm10
from .Coverage import Coverage 
from typing import Optional
from pydantic import Field, BaseModel, constr


class Gwdm11(Gwdm10):
    #overload Coverage with an updated version of it.. 
    coverage: Optional[Coverage] = Field(
        None,
        description='Spatial and Temporal coverage',
        title='Coverage',
    )


