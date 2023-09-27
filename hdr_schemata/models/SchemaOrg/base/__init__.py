from typing import Optional, Union, List
from pydantic import AnyUrl, HttpUrl, BaseModel, RootModel, Field, constr, EmailStr

from .Organization import Organization
from .Person import Person
from .CreativeWork import CreativeWork
from .Place import Place

from hdr_schemata.definitions.SchemaOrg import Text 

    
class Dataset(BaseModel):
    class Config:
        extra = 'forbid'

    m_type: Text = Field(
        alias="@type",
        default="Dataset"
    )

    m_id: Text = Field(
        alias="@id",
        default="Another ID for context"
    )

    m_context: Text = Field(
        alias="@context",
        default="https://schema.org/",
    )
    
    description: Text = Field(
        ...,
        title='description',
        description="A description of the item."
    )

    name: Text = Field(
        ...,
        title='Name',
        description='The name of the item.',
    )

    alternateName: Optional[Union[Text,List[Text]]] = Field(
        ...,
        title='Alternate Name',
        description="Alternative names that have been used to refer to this dataset, such as aliases or abbreviations",
        example=["Quick Draw Dataset", "quickdraw-dataset"]
    )

    creator: Optional[Union[Person,Organization]] = Field(
        ...,
        title='Dataset Creator',
        description="The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork."
    )

    citation: Optional[Union[Text,CreativeWork]] = Field(
        ...,
        title='citation',
        description='A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.'
    )

    funder: Optional[Union[Person,Organization]] = Field(
        ...,
        title='Funder',
        description='A person or organization that supports (sponsors) something through some kind of financial contribution.'
    )

    
