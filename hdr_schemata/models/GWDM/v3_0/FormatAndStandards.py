from typing import List, Optional

from pydantic import BaseModel, Field


class FormatAndStandards(BaseModel):
    class Config:
        extra = "forbid"

    vocabularyEncodingSchemes: Optional[List[str]] = Field(
        None,
        title="Controlled Vocabulary",
        description="Code value of the ontology vocabulary encoding",
        examples=[["OPCS4", "NHS NATIONAL CODES", "ICD10", "OTHER"]],
    )
    conformsTo: Optional[List[str]] = Field(
        None,
        title="Conforms To",
        description="What the vocabulary conforms to.",
        examples=[["LOCAL", "NHS DATA DICTIONARY"]],
    )
    languages: Optional[List[str]] = Field(
        None,
        title="Language Code(s)",
        description="Language code(s) of the language of the dataset metadata and underlying data is made available.",
        examples=[["en"]],
    )
    formats: Optional[List[str]] = Field(
        None,
        title="Dataset Format",
        description="Format(s) the dataset can be made available in",
        examples=["CSV,JSON,SQL database table"],
    )
