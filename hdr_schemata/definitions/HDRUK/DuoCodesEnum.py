from enum import Enum

# Vendored snapshot of the GA4GH Data Use Ontology (DUO).
#
# Generated from ./vendor/duo.csv, itself a copy of
# https://github.com/EBISPOT/DUO/blob/master/duo.csv (last released
# 2021-02-23) - see vendor/README.md for provenance and how to refresh it.
# `hdr_schemata/tests/test_hdruk.py::test_duo_codes_enum_matches_vendored_source`
# parses that file at test time and asserts every row here matches it
# exactly, so this class can't silently drift from what's actually vendored.
#
# `label` appends the code because it is what form hydration renders as the
# option label (via option_titles in the generated *.form.json).

class DuoCodesEnum(Enum):
    def __new__(cls, code, label):
        obj = object.__new__(cls)
        obj._value_ = code
        obj.label = f"{label} ({code})"
        return obj

    DATA_USE_PERMISSION = ("DUO:0000001", "data use permission")
    NRES                = ("DUO:0000004", "no restriction")
    HMB                 = ("DUO:0000006", "health or medical or biomedical research")
    DS                  = ("DUO:0000007", "disease specific research")
    POA                 = ("DUO:0000011", "population origins or ancestry research only")
    RS                  = ("DUO:0000012", "research specific restrictions")
    NMDS                = ("DUO:0000015", "no general methods research")
    GSO                 = ("DUO:0000016", "genetic studies only")
    DATA_USE_MODIFIER   = ("DUO:0000017", "data use modifier")
    NPUNCU              = ("DUO:0000018", "not for profit, non commercial use only")
    PUB                 = ("DUO:0000019", "publication required")
    COL                 = ("DUO:0000020", "collaboration required")
    IRB                 = ("DUO:0000021", "ethics approval required")
    GS                  = ("DUO:0000022", "geographical restriction")
    MOR                 = ("DUO:0000024", "publication moratorium")
    TS                  = ("DUO:0000025", "time limit on use")
    US                  = ("DUO:0000026", "user specific restriction")
    PS                  = ("DUO:0000027", "project specific restriction")
    IS                  = ("DUO:0000028", "institution specific restriction")
    RTN                 = ("DUO:0000029", "return to database or resource")
    GRU                 = ("DUO:0000042", "general research use")
    CC                  = ("DUO:0000043", "clinical care use")
    NPOA                = ("DUO:0000044", "population origins or ancestry research prohibited")
    NPU                 = ("DUO:0000045", "not for profit organisation use only")
    NCU                 = ("DUO:0000046", "non-commercial use only")
