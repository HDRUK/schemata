from datetime import date, datetime
from enum import Enum
from typing import Optional, Union
from pydantic import BaseModel, Field


class AnnotationType(str, Enum):
    duf_score = "duf_score"
    certification = "certification"


class QualityAnnotation(BaseModel):
    class Config:
        extra = "forbid"

    annotationType: Optional[AnnotationType] = Field(
        None,
        title="Annotation Type",
        description="Type of quality evidence: duf_score for Data Utility Framework scores, certification for external certifications.",
    )
    qualityDimension: Optional[str] = Field(
        None,
        title="Quality Dimension",
        description="Quality dimension being assessed, e.g. completeness, accuracy (dqv:inDimension).",
    )
    qualityValue: Optional[str] = Field(
        None,
        title="Quality Value",
        description="Score or grade value for this annotation (dqv:value).",
    )
    qualityDescription: Optional[str] = Field(
        None,
        title="Quality Description",
        description="Human-readable description of the annotation (skos:note).",
    )
    certificationUrl: Optional[str] = Field(
        None,
        title="Certification URL",
        description="Link to the certification document.",
    )
    annotationDate: Optional[Union[date, datetime]] = Field(
        None,
        title="Annotation Date",
        description="Date the annotation was recorded (prov:generatedAtTime).",
    )
