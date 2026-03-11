from __future__ import annotations

from typing import Optional, List

from pydantic import ConfigDict, RootModel


class Icons(RootModel[Optional[List[str]]]):
    model_config = ConfigDict(
        title="Icons",
        json_schema_extra={
            "description": "A list of icon identifiers associated with the dataset, derived from dataset filters."
        },
    )
