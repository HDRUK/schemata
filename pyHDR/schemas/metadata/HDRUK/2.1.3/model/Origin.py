from typing import Optional, List, Union
from pydantic import BaseModel, Field
from definitions import *

class Origin(BaseModel):
    class Config:
        extra = 'forbid'

    purpose: Optional[Union[Optional[CommaSeparatedValues], List[Purpose]]] = Field(
        None,
        description='Pleases indicate the purpose(s) that the dataset was collected.',
        title='Purpose',
    )
    source: Optional[Union[Optional[CommaSeparatedValues], List[Source]]] = Field(
        None,
        description='Pleases indicate the source of the data extraction',
        title='Source',
    )
    collectionSituation: Optional[
        Union[Optional[CommaSeparatedValues], List[Setting]]
    ] = Field(
        None,
        description='Pleases indicate the setting(s) where data was collected. Multiple settings may be provided',
        title='Setting',
    )


