from pydantic import RootModel, constr

class Isocountrycode(RootModel):
    root: constr(pattern=r'^[A-Z]{2}(-[A-Z]{2,3})?$')


