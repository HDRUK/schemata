from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

from .Revision import Revision

class Required(BaseModel):
    gatewayId: constr(min_length=2,max_length=50) = Field(
        ...,
        description='Need a field in Mauro that captures the datasetID to link to gateway database - or can we just use the one created in Mauro?',
        title='Gatewayid',
    )
    gatewayPid: constr(min_length=2,max_length=50) = Field(
        ...,
        description='Need a field in Mauro that captures the dataset pid to link to gateway database',
        title='Gatewaypid',
    )
    issued: datetime = Field(
        ...,
        description="Aren't issued and modified always the same because of versioning? Is that fine to duplicate because datasets in dcat might look different?",
        title='Issued',
    )
    modified: datetime = Field(
        ...,
        description="Aren't issued and modified always the same because of versioning? Is that fine to duplicate because datasets in dcat might look different?",
        title='Modified',
    )

    #note: do we also need to include a 'latest'?
    revisions: List[Revision] = Field(
        ...,
        title='Revisions')


