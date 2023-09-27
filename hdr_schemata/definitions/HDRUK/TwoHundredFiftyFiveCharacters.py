from pydantic import RootModel, constr

class TwoHundredFiftyFiveCharacters(RootModel):
    root: constr(min_length=2, max_length=255)


