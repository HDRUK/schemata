from pydantic import RootModel, constr

class TimePeriod(RootModel):
    root: constr(pattern="^\d{4}-\d{2}-\d{2}\/\d{4}-\d{2}-\d{2}$")
    
