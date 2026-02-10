from __future__ import annotations

from pydantic import ConfigDict, RootModel, constr


class DatasetFilters(
    RootModel[
        list[
            constr(
                pattern=(
                    r'\{\s*"id":\s*"(\d+_){0,5}\d+",\s*"label":\s*".{0,150}",\s*'
                    r'"category":\s*".{0,150}",\s*"primaryGroup":\s*'
                    r'"(cancer-type|data-type|access-type)",\s*"description":\s*".{0,150}"\s*\}'
                )
            )
        ]
    ]
):
    model_config = ConfigDict(
        title="Dataset Filters",
        json_schema_extra={"description": "A list of categorization tags (ids) for the dataset."},
    )
