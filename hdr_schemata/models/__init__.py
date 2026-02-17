


# - There is a problem with pydantic v2 where the 'exclude' feature doesnt currently work
#   see: https://github.com/pydantic/pydantic/discussions/2686
# - This hack means that I can inherit from the Schema.Org model but then exclude fields
#   that are not needed for the BioSchema

def _safe_remove_field(cls, field):
    fields_set = getattr(cls, "model_fields_set", None)
    if hasattr(fields_set, "deleter"):
        fields_set.deleter(field)
    elif hasattr(fields_set, "discard"):
        fields_set.discard(field)

    computed_fields = getattr(cls, "model_computed_fields", None)
    if hasattr(computed_fields, "deleter"):
        computed_fields.deleter(field)
    elif hasattr(computed_fields, "pop"):
        computed_fields.pop(field, None)

    fields = getattr(cls, "model_fields", None)
    if hasattr(fields, "pop"):
        fields.pop(field, None)


def filter_fields_in_cls(cls,fields_to_keep):
    all_keys = list(cls.model_fields.keys())
    for field in all_keys:
        if field in fields_to_keep: continue        
        _safe_remove_field(cls, field)
        
    for field in fields_to_keep:
        if not field in cls.model_fields.keys():
            raise NotImplementedError(f'Field "{field}" has not been implemented!')

    #also force rebuild of model schema
    cls.__pydantic_complete__ = False
    if hasattr(cls, "__pydantic_core_schema__"):
        del cls.__pydantic_core_schema__
    cls.model_rebuild(force=True)

def remove_fields_from_cls(cls,fields):
    for field in fields:
        if not field in fields: continue        
        _safe_remove_field(cls, field)

    #also force rebuild of model schema
    cls.__pydantic_complete__ = False
    if hasattr(cls, "__pydantic_core_schema__"):
        del cls.__pydantic_core_schema__
    cls.model_rebuild(force=True)

