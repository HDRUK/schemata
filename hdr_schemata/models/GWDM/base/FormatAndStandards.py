from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

class FormatAndStandards(BaseModel):
    class Config:
        extra = 'forbid'

    #note: should be limited to allowed values?
    #      see: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/ControlledVocabularyEnum.py
    vocabularyEncodingSchemes:  Optional[CommaSeparatedValues] = Field(
        ...,
        description='Code value of the ontology vocabulary encoding',
        example="OPCS4,NHS NATIONAL CODES,ICD10,OTHER"
        title='Controlled Vocabulary',
    )

    #note: dont really know what this means, conforms to 'NHS DATA DICTIONARY' what does that mean?!?
    conformsTo: Optional[CommaSeparatedValues] = Field(
        ...,
        description='What the vocabulary conforms to.',
        example="LOCAL,NHS DATA DICTIONARY",
        title='Conforms To',
    )

    #note: may need to limit these (en,fr,es,po,..) instead of arbitrary CommaSeparatedValues
    #      see: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/LanguageEnum.py
    languages: Optional[CommaSeparatedValues] = Field(
        ...,
        description='Language code(s) of the language of the dataset metadata and underlying data is made available.',
        example="en"
        title='Language Code(s)',
    )

    #note: this is surely dependent on the AccessService?
    #      e.g. SAIL will let you access via SQL only
    #note: may need to limit these to specific Enum formats instead of CommaSeparatedValues
    #      'SQL database table' --> some really poor choices of 'formats'
    formats: Optional[CommaSeparatedValues] = Field(
        ...,
        description='Format(s) the dataset can be made available in',
        example="CSV,JSON,SQL database table",
        title='Dataset Format',
    )
