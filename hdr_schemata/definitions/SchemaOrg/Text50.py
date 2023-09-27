from pydantic import RootModel, constr

class Text50(RootModel):
    root: constr(min_length=50,max_length=5000)
    
