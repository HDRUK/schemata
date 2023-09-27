from typing import Optional, Union, List
from pydantic import AnyUrl, HttpUrl, BaseModel, RootModel, Field, constr, EmailStr

from .Organization import Organization
from .Person import Person

from hdr_schemata.definitions.SchemaOrg import Text, Text50

    
class Dataset(BaseModel):
    class Config:
        extra = 'forbid'

    _type: Text = Field(
        alias="@type",
        default="Dataset"
    )
    
    description: Text50 = Field(
        ...,
        title='description',
        description=r'''A short summary describing a dataset.
        Guidelines

        The summary must be between 50 and 5000 characters long.
        The summary may include Markdown syntax. Embedded images need to use absolute path URLs (instead of relative paths).
        When using the JSON-LD format, denote new lines with \n (two characters: backslash and lower case letter "n").
        '''
    )

    name: Text = Field(
        ...,
        title='Name',
        description=r'''A descriptive name of a dataset. For example, "Snow depth in the Northern Hemisphere".
        Guidelines
        
        Use unique names for distinct datasets whenever possible.
        Recommended: "Snow depth in the Northern Hemisphere" and "Snow depth in the Southern Hemisphere" for two different datasets.
        
        Not recommended: "Snow depth" and "Snow depth" for two different datasets.
        '''
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
        description="The creator or author of this dataset. To uniquely identify individuals, use ORCID ID as the value of the sameAs property of the Person type. To uniquely identify institutions and organizations, use ROR ID.",
        example= [
            {
                "@type": "Person",
                "sameAs": "https://orcid.org/0000-0000-0000-0000",
                "givenName": "Jane",
                "familyName": "Foo",
                "name": "Jane Foo"
            },
            {
                "@type": "Person",
                "sameAs": "https://orcid.org/0000-0000-0000-0001",
                "givenName": "Jo",
                "familyName": "Bar",
                "name": "Jo Bar"
            },
            {
                "@type": "Organization",
                "sameAs": "https://ror.org/xxxxxxxxx",
                "name": "Fictitious Research Consortium"
            }
        ]
    )
