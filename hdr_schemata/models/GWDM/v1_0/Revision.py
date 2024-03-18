from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.annotations import annotations

an = annotations.GWDM.v1p0.required.revisions


class Revision(BaseModel):

    version: constr(min_length=2, max_length=100) = Field(
        ...,
        description=an.version.description,
        example="6.0.0",
        title=an.version.title,
    )

    url: Url = Field(
        ...,
        description=an.url.description,
        example="https://api.service.nhs.uk/health-research-data-catalogue/datasetrevisions/841f7da2-b018-41f6-b4ae-2e0aadab6561",
        title=an.url.title,
    )
