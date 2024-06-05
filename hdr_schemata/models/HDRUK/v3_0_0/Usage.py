from hdr_schemata.models.HDRUK.v2_1_2.Usage import Usage as BaseUsage
from hdr_schemata.models import remove_fields_from_cls
from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *
from .annotations import annotations

an = annotations.accessibility.usage


class Usage(BaseUsage):

    dataUseLimitation: Optional[List[DataUseLimitationV2]
    ] = Field(None, **an.dataUseLimitation.__dict__)

    dataUseRequirements: Optional[List[DataUseRequirementsV2]
    ] = Field(None, **an.dataUseRequirements.__dict__)

    resourceCreator: Optional[
        Union[Optional[ShortDescription], List[Optional[ShortDescription]]]
    ] = Field(None, **an.resourceCreator.__dict__)

    investigations: Optional[List[Url]] = Field(None, **an.investigations.__dict__)

    publicationAboutDataset: Optional[List[Doi]
    ] = Field(None, **an.publicationAboutDataset.__dict__)

    publicationUsingDataset: Optional[List[Doi]
    ] = Field(None, **an.publicationUsingDataset.__dict__)

remove_fields_from_cls(Usage, ["isReferencedBy"])