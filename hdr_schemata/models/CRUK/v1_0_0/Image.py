from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import Description


class Image(BaseModel):
    class Config:
        extra = "forbid"

    image: Optional[str] = Field(
        None,
        title="Image",
        description="An image file.",
        json_schema_extra={
            "contentMediaType": "image/*",
            "guidance": "Upload an image file (PNG, JPG, SVG) Max file size: 5MB.",
        },
    )

    description: Optional[Description] = None
