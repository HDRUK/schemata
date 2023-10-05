from hdr_schemata.models.GWDM import Gwdm10
from .Coverage import Coverage 
from .Accessibility import Accessibility
from typing import Optional
from pydantic import Field, BaseModel, constr


class Gwdm11(Gwdm10):
    #overload Coverage with an updated version of it.. 
    coverage: Optional[Coverage] = Field(
        None,
        description='Spatial and Temporal coverage',
        title='Coverage',
    )

    #modifying Accessibility --> modifying Usage
    accessibility: Accessibility = Field(
        None,
        description='Accessibility information.',
        title='Accessibility',
    )

