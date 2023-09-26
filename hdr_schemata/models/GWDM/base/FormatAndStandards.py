from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

class FormatAndStandards(BaseModel):
    class Config:
        extra = 'forbid'

    vocabularyEncodingSchemes:  Optional[CommaSeparatedValues] = Field(
        ...,
        description='.',
        title='Controlled Vocabulary',
    )
    conformsTo: Optional[CommaSeparatedValues] = Field(
        ...,
        description='.',
        title='Conforms To',
    )
    languages: Optional[CommaSeparatedValues] = Field(
        ...,
        description='This should list all the languages in which the dataset metadata and underlying data is made available.',
        title='Language',
    )
    formats: Optional[CommaSeparatedValues] = Field(
        ...,
        description='.',
        title='Format',
    )
