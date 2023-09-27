from typing import Union
from pydantic import BaseModel, Field, AnyUrl

from hdr_schemata.definitions.SchemaOrg import Text,Ror

class Organization(BaseModel):
    
    _type: Text = Field(
        alias="@type",
        default="Organization"
    )

    sameAs: AnyUrl = Field(
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.",
        example="https://www.kaggle.com/datasets/meirnizri/covid19-dataset"
    )
    
    name: Text = Field(
        description="Name of the organisation",
        example="Fictitious Research Consortium"
    )

