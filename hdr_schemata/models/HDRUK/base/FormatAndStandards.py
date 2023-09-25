from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

class FormatAndStandards(BaseModel):
    class Config:
        extra = 'forbid'

    vocabularyEncodingScheme: Union[
        Optional[CommaSeparatedValues], List[ControlledVocabulary]
    ] = Field(
        ...,
        description='List any relevant terminologies / ontologies / controlled vocabularies, such as ICD 10 Codes, NHS Data Dictionary National Codes or SNOMED CT International, that are being used by the dataset. If the controlled vocabularies are local standards, please make that explicit. If you are using a standard that has not been included in the list, please use “other” and contact support desk to ask for an addition. Notes: More than one vocabulary may be provided.',
        title='Controlled Vocabulary',
    )
    conformsTo: Union[
        Optional[CommaSeparatedValues], List[StandardisedDataModels]
    ] = Field(
        ...,
        description='List standardised data models that the dataset has been stored in or transformed to, such as OMOP or FHIR. If the data is only available in a local format, please make that explicit. If you are using a standard that has not been included in the list, please use “other” and contact support desk to ask for an addition.',
        title='Conforms To',
    )
    language: Union[Optional[CommaSeparatedValues], List[Language]] = Field(
        ...,
        description='This should list all the languages in which the dataset metadata and underlying data is made available.',
        title='Language',
    )
    format: Union[Optional[CommaSeparatedValues], List[Format]] = Field(
        ...,
        description='If multiple formats are available please specify. See application, audio, image, message, model, multipart, text, video, https://www.iana.org/assignments/media-types/media-types.xhtml Note: If your file format is not included in the current list of formats, please indicate other. If you are using the HOP you will be directed to a service desk page where you can request your additional format. If not please go to: https://metadata.atlassian.net/servicedesk/customer/portal/4 to request your format.',
        title='Format',
    )
