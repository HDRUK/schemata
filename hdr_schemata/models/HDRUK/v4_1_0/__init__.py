from hdr_schemata.models.HDRUK.v4_0_0 import Hdruk400
import json
from pydantic import Field

from .Accessibility import Accessibility


class Hdruk410(Hdruk400):

    accessibility: Accessibility = Field(
        ..., description=Hdruk400.model_fields["accessibility"].description,
        title=Hdruk400.model_fields["accessibility"].title,
    )

    @classmethod
    def save_schema(cls, location="./4.1.0/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
