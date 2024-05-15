from pydantic import RootModel, constr

class MeasuredProperty(RootModel):
    root: constr(min_length=1, max_length=100)


