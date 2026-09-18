import json
from pydantic import Field

from hdr_schemata.models.GWDM.v2_1 import Gwdm21

from .Accessibility import Accessibility


class Gwdm22(Gwdm21):
    accessibility: Accessibility = Field(
        ..., description=Gwdm21.model_fields["accessibility"].description,
        title=Gwdm21.model_fields["accessibility"].title,
    )

    @classmethod
    def save_schema(cls, location: str = "./2.2/schema.json") -> None:
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
