from typing import List, Optional

from pydantic import BaseModel, Field

from .Organisation import Organisation


class Usage(BaseModel):
    class Config:
        extra = "forbid"

    dataUseLimitation: Optional[List[str]] = Field(
        None,
        title="Data use limitation",
        description="Please provide an indication of consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. NOTE: we have extended the Data Use Ontology to include a value for NO LINKAGE.",
        json_schema_extra={
            "guidance": (
                "Please provide an indication of consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used.\n"
                "- **General research use**: This data use limitation indicates that use is allowed for general research use for any research purpose.\n"
                "- **No restriction**: This data use limitation indicates there is no restriction on use.\n"
                "- **Research use only**: This data use limitation indicates that use is limited to research purposes.\n"
                "- **No linkage**: This data use limitation indicates there is a restriction on linking to any other datasets"
            )
        },
    )
    dataUseRequirements: Optional[List[str]] = Field(
        None,
        title="Data use requirements",
        description="Please indicate fit here are any additional conditions set for use if any, multiple requirements may be provided. Please ensure that these restrictions are documented in access rights information.",
        json_schema_extra={
            "guidance": (
                "- Please indicate if there are any additional conditions set for use if any, multiple requirements may be provided.\n"
                "- Please ensure that these restrictions are documented in access rights information."
            )
        },
    )
    resourceCreator: Optional[Organisation] = Field(
        None,
        title="Citation requirements",
        description="Please provide the text that you would like included as part of any citation that credits this dataset. This is typically just the name of the publisher.   No employee details should be provided.",
        examples=["National Services Scotland"],
    )
