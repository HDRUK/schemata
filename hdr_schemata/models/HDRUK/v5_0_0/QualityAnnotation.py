from datetime import date, datetime
from typing import Literal, Optional, Union

from pydantic import BaseModel, Field


AnnotationType = Literal["duf_score", "certification"]


class QualityAnnotation(BaseModel):
    class Config:
        extra = "forbid"

    annotationType: Optional[AnnotationType] = Field(
        None,
        title="Annotation Type",
        description="Category of quality annotation: 'duf_score' for a numeric quality score, or 'certification' for a formal certification.",
    )
    qualityDimension: Optional[str] = Field(
        None,
        title="Quality Dimension",
        description="The quality dimension being measured, e.g. completeness, accuracy, timeliness (dqv:inDimension).",
    )
    qualityValue: Optional[str] = Field(
        None,
        title="Quality Value",
        description="The score, grade, or pass/fail result for this quality annotation (dqv:value).",
    )
    qualityDescription: Optional[str] = Field(
        None,
        title="Quality Description",
        description="Human-readable description of the quality annotation (skos:note).",
    )
    certificationUrl: Optional[str] = Field(
        None,
        title="Certification URL",
        description="URL linking to the full certification or assessment report.",
    )
    annotationDate: Optional[Union[date, datetime]] = Field(
        None,
        title="Annotation Date",
        description="Date when this quality annotation was recorded (prov:generatedAtTime).",
    )
