from typing import Optional, Union, List
from pydantic import AnyUrl, HttpUrl, BaseModel, RootModel, Field, constr, EmailStr
from pydantic import ConfigDict

from .Organization import Organization
from .Person import Person
from .CreativeWork import CreativeWork
from .Place import Place
from .DataDownload import DataDownload
from .DataCatalog import DataCatalog

from hdr_schemata.definitions.SchemaOrg import Text, Text50, Number 
from hdr_schemata.definitions.SchemaOrg import SingleDate, TimePeriod, OpenEndedTimePeriod
    
    
class Dataset(BaseModel):

    model_config = ConfigDict(extra='forbid')

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

    distribution: Optional[DataDownload] = Field(
        ...,
        title='distribution',
        description="A downloadable form of this dataset, at a specific location, in a specific format. This property can be repeated if different variations are available. There is no expectation that different downloadable distributions must contain exactly equivalent information (see also DCAT on this point). Different distributions might include or exclude different subsets of the entire dataset, for example"
    )

    includedInDataCatalog = Optional[DataCatalog] = Field(
        ...,
        title='Included In Data Catalog',
        description="A data catalog which contains this dataset. Supersedes includedDataCatalog, catalog. Inverse property: dataset"
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
    
    isPartOf: Optional[Union[AnyUrl,CreativeWork]] = Field(
        None,
        title='Is Part Of (dataset)',
        description="If the dataset is a collection of smaller datasets, use the hasPart property to denote such relationship. Conversly, if the dataset is part of a larger dataset, use isPartOf. Both properties can take the form of a URL or a Dataset instance. In case Dataset is used as a value it has to include all of the properties required for a standalone Dataset. ",
        examples=["https://example.com/aggregate_dataset"]
    )

    hasPart: Optional[CreativeWork] = Field(
        None,
        title='Has Part',
        description="Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense)."
    )
    
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
