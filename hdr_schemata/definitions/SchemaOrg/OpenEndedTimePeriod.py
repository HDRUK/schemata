from datetime import date
from pydantic import RootModel, constr

class OpenEndedTimePeriod(RootModel):
    root: constr(pattern="^\d{4}-\d{2}-\d{2}\/\.\.$")

