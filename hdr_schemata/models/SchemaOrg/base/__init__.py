from typing import Optional, Union, List
from pydantic import AnyUrl, HttpUrl, BaseModel, RootModel, Field, constr, EmailStr

from .Organization import Organization
from .Person import Person

from hdr_schemata.definitions.SchemaOrg import Text, Text

    
class Dataset(BaseModel):
    class Config:
        extra = 'forbid'

    _type: Text = Field(
        alias="@type",
        default="Dataset"
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
