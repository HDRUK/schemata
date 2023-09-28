from typing import Optional, Union, List
from pydantic import AnyUrl, HttpUrl, BaseModel, RootModel, Field, constr, EmailStr

#import base models
from hdr_schemata.models.SchemaOrg.base import Dataset as BaseDataset
from hdr_schemata.models.SchemaOrg.base import Person, CreativeWork, Place

#import a different version of the Organization model - a Google Recommened one
from .Organization import Organization

#import definitions
from hdr_schemata.definitions.SchemaOrg import Text, Text50, Number
from hdr_schemata.definitions.SchemaOrg import SingleDate, TimePeriod, OpenEndedTimePeriod
    
class Dataset(BaseDataset):
    """
    - inherits from the baseline Schema.org definitions (currently incomplete)
    - implements some additional Google Recommended specific patterns 
    """
    
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
    #creator: Optional[Union[Person,Organization]] = Field(
    creator: Optional[Organization] = Field(
        None,
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

    #overload with google examples and description
    citation: Optional[Union[Text,CreativeWork]] = Field(
        None,
        title='citation',
        description="Identifies academic articles that are recommended by the data provider be cited in addition to the dataset itself. Provide the citation for the dataset itself with other properties, such as name, identifier, creator, and publisher properties. For example, this property can uniquely identify a related academic publication such as a data descriptor, data paper, or an article for which this dataset is supplementary material for. Don't use this property to provide citation information for the dataset itself. It is intended to identify related academic articles, not the dataset itself. To provide information necessary to cite the dataset itself use name, identifier, creator, and publisher properties instead.",
        examples=[
            "https://doi.org/10.1111/111",
            "https://identifiers.org/pubmed:11111111",
            "https://identifiers.org/arxiv:0111.1111v1",
            "Doe J (2014) Influence of X ... https://doi.org/10.1111/111"
        ]
    )

    #overload with google examples
    #funder: Optional[Union[Person,Organization]] = Field(
    funder: Optional[Organization] = Field(
        None,
        title='Funder',
        description='A person or organization that provides financial support for this dataset. To uniquely identify individuals, use ORCID ID as the value of the sameAs property of the Person type. To uniquely identify institutions and organizations, use ROR ID.',
        examples=[
            {
                "@type": "Person",
                "sameAs": "https://orcid.org/0000-0000-0000-0002",
                "givenName": "Jane",
                "familyName": "Funder",
                "name": "Jane Funder"
            },
            {
                "@type": "Organization",
                "sameAs": "https://ror.org/yyyyyyyyy",
                "name": "Fictitious Funding Organization"
            }
        ]
    )

    #not implemented in the "base" yet...
    #google recommendation to also implement hasPart if the dataset is a subset of a larger set
    isPartOf: Optional[AnyUrl] = Field(
        None,
        title='Is Part Of (dataset)',
        description="If the dataset is a collection of smaller datasets, use the hasPart property to denote such relationship. Conversly, if the dataset is part of a larger dataset, use isPartOf. Both properties can take the form of a URL or a Dataset instance. In case Dataset is used as a value it has to include all of the properties required for a standalone Dataset. ",
        examples=["https://example.com/aggregate_dataset"]
    )

    #not implemented in the "base" yet...
    #google says to use URL, Text, or PropertyValue and could be a list of these
    #... overly complex, we may want to limit this? Or not care as we'll never have lists of identifiers...
    identifier: Optional[Union[AnyUrl,Text,List[Union[AnyUrl,Text]]]] = Field(
        None,
        title='identifier',
        description='An identifier, such as a DOI or a Compact Identifier. If the dataset has more than one identifier, repeat the identifier property. If using JSON-LD, this is represented using JSON list syntax.'
    )

    isAccessibleForFree: Optional[bool] = Field(
        None,
        title='Is Accessible For Free?',
        description='Whether the dataset is accessible without payment.'
    )

    keywords: Optional[Union[Text,List[Text]]] = Field(
        None,
        title='Keywords',
        description='Keywords summarizing the dataset.',
        examples= [
            [
                "ATMOSPHERE > ATMOSPHERIC PHENOMENA > CYCLONES",
                "ATMOSPHERE > ATMOSPHERIC PHENOMENA > DROUGHT",
                "ATMOSPHERE > ATMOSPHERIC PHENOMENA > FOG",
                "ATMOSPHERE > ATMOSPHERIC PHENOMENA > FREEZE"
            ]
        ]
    )

    license: Optional[Union[AnyUrl,CreativeWork]] = Field(
        None,
        title='License',
        description='A license under which the dataset is distributed. Provide a URL that unambiguously identifies a specific version of the license used. e.g. https://creativecommons.org/licenses/by/4.0 not https://creativecommons.org/licenses/by',
        examples=[
            "https://creativecommons.org/publicdomain/zero/1.0/",
            {
                "@type": "CreativeWork",
                "name": "Custom license",
                "url": "https://example.com/custom_license"
            }
        ]
    )

    measurementTechnique: Optional[Union[Text,AnyUrl]] = Field(
        None,
        title='Measurement Technique',
        description='The technique, technology, or methodology used in a dataset, which can correspond to the variable(s) described in variableMeasured.'
    )

    sameAs: Optional[Union[AnyUrl,List[AnyUrl]]] = Field(
        None,
        title='Same As (dataset)',
        description="The URL of a reference web page that unambiguously indicates the dataset's identity."
    )

    spatialCoverage: Optional[Union[Text,Place]] = Field(
        None,
        title='Spatial Coverage',
        description="You can provide a single point that describes the spatial aspect of the dataset. Only include this property if the dataset has a spatial dimension. For example, a single point where all the measurements were collected, or the coordinates of a bounding box for an area.",
        examples=[
            {
                "@type": "Place",
                "geo": {
                    "@type": "GeoShape",
                    "box": "39.3280 120.1633 40.445 123.7878"
                }
            }
        ]
    )

    temporalCoverage: Optional[Union[SingleDate,TimePeriod,OpenEndedTimePeriod]] = Field(
        None,
        title='Temporal Coverage',
        description='The data in the dataset covers a specific time interval. Only include this property if the dataset has a temporal dimension. Schema.org uses the ISO 8601 standard to describe time intervals and time points. You can describe dates differently depending upon the dataset interval. Indicate open-ended intervals with two decimal points (..).'
    )

    variableMeasured: Optional[Text] = Field(
        None,
        title='Variable Measured',
        description='The variable that this dataset measures. For example, temperature or pressure.'
    )

    version: Optional[Union[Text,Number]] = Field(
        None,
        title='version',
        description='The version number for the dataset.'
    )
    
    url: Optional[AnyUrl] = Field(
        None,
        title='url',
        description='Location of a page describing the dataset.'
    )
    
        
__fields_to_keep = [
    "m_type",
    "m_id",
    "m_context",
    "description",
    "name",
    "alternateName",
    "creator",
    "citation",
    "funder",
    "hasPart or isPartOf",
    "identifier",
    "isAccessibleForFree",
    "keywords",
    "license",
    "measurementTechnique",
    "sameAs",
    "spatialCoverage",
    "temporalCoverage",
    "variableMeasured",
    "version",
    "url",
    "distribution",
]

# - There is a problem with pydantic v2 where the 'exclude' feature doesnt currently work
#   see: https://github.com/pydantic/pydantic/discussions/2686
# - This hack means that I can inherit from the Schema.Org model but then exclude fields
#   that are not needed for the BioSchema
all_keys = list(Dataset.model_fields.keys())
for field in all_keys:
    if not field in __fields_to_keep:
        if type(Dataset.__fields_set__) == set:
            Dataset.__fields_set__.remove(field)
        del Dataset.model_fields[field]

for field in __fields_to_keep:
    if not field in Dataset.model_fields.keys():
        raise NotImplementedError(f'Field "{field}" has not been implemented!')
