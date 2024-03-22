from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards


class FormatAndStandards(BaseModel):
    class Config:
        extra = "forbid"

    # note: should be limited to allowed values?
    #      see: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/ControlledVocabularyEnum.py
    vocabularyEncodingSchemes: Optional[CommaSeparatedValues] = Field(
        ..., **an.vocabularyEncodingSchemes.__dict__
    )

    # note: dont really know what this means, conforms to 'NHS DATA DICTIONARY' what does that mean?!?
    conformsTo: Optional[CommaSeparatedValues] = Field(..., **an.conformsTo.__dict__)

    # note: may need to limit these (en,fr,es,po,..) instead of arbitrary CommaSeparatedValues
    #      see: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/LanguageEnum.py
    languages: Optional[CommaSeparatedValues] = Field(..., **an.languages.__dict__)

    # note: this is surely dependent on the AccessService?
    #      e.g. SAIL will let you access via SQL only
    # note: may need to limit these to specific Enum formats instead of CommaSeparatedValues
    #      'SQL database table' --> some really poor choices of 'formats'
    formats: Optional[CommaSeparatedValues] = Field(..., **an.formats.__dict__)
