from pydantic import constr,RootModel

class Uuidv4(RootModel):
    root: constr(
        pattern=r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$',
        min_length=36,
        max_length=36,
    )


