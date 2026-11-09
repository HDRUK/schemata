from pydantic import RootModel, conint

class Year(RootModel):
    root: conint(ge=1900, le=2100)
