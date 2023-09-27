from typing import Optional, Union, List
from pydantic import AnyUrl, HttpUrl, BaseModel, RootModel, Field, constr, EmailStr

#import base models
from hdr_schemata.models.SchemaOrg.base import Dataset as BaseDataset
from hdr_schemata.models.SchemaOrg.base import Person

#import a different version of the Organization model - a Google Recommened one
from .Organization import Organization

#import definitions
from hdr_schemata.definitions.SchemaOrg import Text, Text50

    
class Dataset(BaseDataset):

    #overload description to be limited to a minimum of 50
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

    #overload the name with some more description/recommendation
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

    #overload the creator to be a GoogleRecommended Organization which is a bit different from the base Schema.org 
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

