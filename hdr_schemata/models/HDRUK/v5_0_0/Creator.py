from typing import Optional

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import Url


class Creator(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[str] = Field(
        None,
        title="Creator Name",
        description="Name of the person or organisation that created the dataset (foaf:name).",
    )
    rorId: Optional[Url] = Field(
        None,
        title="ROR ID",
        description="Research Organization Registry identifier URI, e.g. https://ror.org/XXXXXXXX.",
    )
    orcidId: Optional[Url] = Field(
        None,
        title="ORCID ID",
        description="ORCID identifier URI, e.g. https://orcid.org/XXXX-XXXX-XXXX-XXXX.",
    )
    gatewayId: Optional[str] = Field(
        None,
        title="Gateway ID",
        description="HDR UK Gateway identifier for the creator organisation.",
    )
