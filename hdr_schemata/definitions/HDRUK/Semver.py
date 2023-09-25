from pydantic import constr,RootModel

class Semver(RootModel):
    root: constr(pattern=r'^([0-9]+)\.([0-9]+)\.([0-9]+)$')

    
