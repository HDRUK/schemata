from typing import Optional, Union, List
from pydantic import AnyUrl, BaseModel, RootModel, Field,  EmailStr

from hdr_schemata.definitions.SchemaOrg import Text

class DataDownload(BaseModel):

    m_type: Text = Field(
        alias="@type",
        default="DataDownload"
    )

    contentUrl: AnyUrl = Field(
        ...,
        description="Actual bytes of the media object, for example the image file or video file."
    )

    encodingFormat: Optional[Union[Text,AnyUrl,List[Text],List[AnyUrl]]] = Field(
        default="Unknown",
        description=r'''Media type typically expressed using a MIME format (see IANA site and MDN reference), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc. 
In cases where a CreativeWork has several media type representations, encoding can be used to indicate each MediaObject alongside particular encodingFormat information.

Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry. Supersedes fileFormat.''',
        examples=['CSV','XML']
    )

    
