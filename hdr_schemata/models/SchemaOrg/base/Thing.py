from typing import Optional
from pydantic import BaseModel, Field, AnyUrl

from hdr_schemata.definitions.SchemaOrg import Text

class Thing(BaseModel):
    
    name: Optional[Text] = Field(
        None,
        description="Name of the organisation",
        example="Fictitious Research Consortium"
    )

    description: Optional[Text] = Field(
        None,
        description="A description of the item."
    )

    identifier: Optional[Text] = Field(
        None,
        description="The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See background notes for more details."
    )

    sameAs: Optional[AnyUrl] = Field(
        None,
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.",
        example="https://www.kaggle.com/datasets/meirnizri/covid19-dataset"
    )
    

    
