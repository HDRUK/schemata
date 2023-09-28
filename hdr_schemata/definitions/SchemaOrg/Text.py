from pydantic import RootModel, constr

class Text(RootModel):
    root: constr()
    
