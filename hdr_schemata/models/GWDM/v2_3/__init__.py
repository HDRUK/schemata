import json
from typing import Optional
from pydantic import Field

from hdr_schemata.models.GWDM.v2_2 import Gwdm22

from .Linkage import Linkage
from .Population import Population

from .annotations import annotations as an


class Gwdm23(Gwdm22):
    linkage: Optional[Linkage] = Field(
        None, description=Gwdm22.model_fields["linkage"].description,
        title=Gwdm22.model_fields["linkage"].title,
    )

    population: Optional[Population] = Field(
        None, description=an.population.description, title=an.population.title
    )

    @classmethod
    def save_schema(cls, location: str = "./2.3/schema.json") -> None:
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
