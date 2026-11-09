from pydantic import Field, RootModel, constr

class RichText(RootModel):
    root: constr(min_length=1, max_length=50000) = Field(
        ..., json_schema_extra={"contentMediaType": "text/html"}
    )
