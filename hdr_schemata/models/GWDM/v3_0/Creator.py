from typing import Optional
from pydantic import BaseModel, Field


class Creator(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[str] = Field(
        None,
        title="Creator Name",
        description="Display name of the entity responsible for creating the dataset (foaf:name).",
    )
    rorId: Optional[str] = Field(
        None,
        title="Creator ROR ID",
        description="Research Organisation Registry identifier for the creator organisation.",
    )
    orcidId: Optional[str] = Field(
        None,
        title="Creator ORCID",
        description="ORCID identifier for the creator individual.",
    )
    gatewayId: Optional[str] = Field(
        None,
        title="Creator Gateway ID",
        description="HDR UK Gateway internal identifier for the creator.",
    )
