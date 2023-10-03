from typing import Optional, Union
from pydantic import AnyUrl, BaseModel, RootModel, Field,  EmailStr

from hdr_schemata.definitions.SchemaOrg import Text

from .Person import Person
from .Organization import Organization

class CreativeWork(BaseModel):

    m_type: Text = Field(
        alias="@type",
        default="CreativeWork"
    )

    name: Text = Field(
        ...,
        description="The name of the item."
    )

    abstract: Optional[Text] = Field(
        None,
        title='abstract',
        description="An abstract is a short description that summarizes a CreativeWork."
    )
    
    identifier: Text = Field(
        ...,
        description="The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links."
    )


    creator: Optional[Union[Person,Organization]] = Field(
        ...,
        title='Creative Work creator',
        description="The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork."
    )

    publisher: Optional[Union[Person,Organization]] = Field(
        ...,
        title='Creative Work publisher',
        description="The publisher of the creative work."
    )

    
