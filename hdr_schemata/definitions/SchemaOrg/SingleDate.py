from datetime import date
from pydantic import RootModel, constr

class SingleDate(RootModel):
    root: date
    
