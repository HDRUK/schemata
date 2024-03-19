from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.annotations import annotations

an = annotations.HDRUK.v2p1p2.enrichmentAndLinkage


class EnrichmentAndLinkage(BaseModel):
    class Config:
        extra = "forbid"

    qualifiedRelation: Optional[
        Union[
            Optional[CommaSeparatedValues],
            List[Union[Optional[Url], OneHundredFiftyCharacters]],
        ]
    ] = Field(None, **an.qualifiedRelation.__dict__)
    derivation: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[AbstractText]]]
    ] = Field(None, **an.derivation.__dict__)
    tools: Optional[Union[Optional[CommaSeparatedValues], List[Optional[Url]]]] = Field(
        None, **an.tools.__dict__
    )
