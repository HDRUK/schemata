from pydantic import RootModel, constr

#just a place holder for now......
class Number(RootModel):
    root: constr()
    
