from pydantic import RootModel, constr

class OneHundredFiftyCharacters(RootModel):
    root: constr(min_length=2, max_length=150)


