from pydantic import constr,RootModel

class Ror(RootModel):
    root:  constr(
        pattern=r'^https:\/\/ror\.org.*$'
    )
