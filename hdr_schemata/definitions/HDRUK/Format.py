from pydantic import RootModel, constr

class Format(RootModel):
    root: constr(min_length=1)


