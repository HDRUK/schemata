from typing import Optional, Union
from pydantic import AnyUrl, BaseModel, RootModel, Field,  EmailStr

from hdr_schemata.definitions.SchemaOrg import Text

from .Organization import Organization


class Person(BaseModel):

    m_type: Text = Field(
        alias="@type",
        default="Person"
    )
    
    sameAs: Optional[AnyUrl] = Field(
        ...,
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.",
        example="https://orcid.org/0000-0000-0000-0000"
    )
        
    name: Text = Field(
        ...,
        description="Full name of a person",
        example="Jane Foo"
    )
        
    givenName: Optional[Text] = Field(
        ...,
        description="Given name. In the U.S., the first name of a Person.",
        example="Jane"
    )
        
    familyName: Optional[Text] = Field(
        ...,
        description="Family name. In the U.S., the last name of a Person.",
        example="Foo"
    )
        
    email: Optional[EmailStr] = Field(
        ...,
        description="Email address",
        example="blah@google.com"
    )
    affiliation: Organization = Field(
        ...,
        description="An organization that this person is affiliated with. For example, a school/university, a club, or a team."
    )

