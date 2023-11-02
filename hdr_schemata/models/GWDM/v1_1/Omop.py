from typing import Optional
from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import CommaSeparatedIntegers

class OmopIDs(BaseModel):
    measurements: Optional[CommaSeparatedIntegers] = Field(
        None,
        description="OMOP Concept IDs for measured quantities. E.g. 44810410 - https://athena.ohdsi.org/search-terms/terms/44810410",
        example="44810410",
        title="OMOP Measurements"
    )
    
    drug: Optional[CommaSeparatedIntegers] = Field(
        None,
        description="OMOP Concept IDs for drug exposures. E.g. 602396 - https://athena.ohdsi.org/search-terms/terms/602396",
        example="602396",
        title="OMOP Drugs"
    )

    observations: Optional[CommaSeparatedIntegers] = Field(
        None,
        description="OMOP Concept IDs for observations.",
        example="12345,6789",
        title="OMOP Observations"
    )

    specimens: Optional[CommaSeparatedIntegers] = Field(
        None,
        description="OMOP Concept IDs for specimens.",
        example="12345,6789",
        title="OMOP Specimens"
    )

    conditions: Optional[CommaSeparatedIntegers] = Field(
        None,
        description="OMOP Concept IDs for condition occurrences.",
        example="12345,6789",
        title="OMOP Condition Occurrences"
    )

    procedures: Optional[CommaSeparatedIntegers] = Field(
        None,
        description="OMOP Concept IDs for procedure occurrences.",
        example="12345,6789",
        title="OMOP Procedure Occurrences"
    )

    device_exposures: Optional[CommaSeparatedIntegers] = Field(
        None,
        description="OMOP Concept IDs for device exposures.",
        example="12345,6789",
        title="OMOP "
    )

