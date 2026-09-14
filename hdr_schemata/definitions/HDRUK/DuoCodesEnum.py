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
# Each member carries its DUO id (the enum value - what validates/serializes,
# unchanged), its shorthand (`.shortcode` - DUO's own short mnemonic, e.g.
# "GRU"; empty string for the two abstract parent terms that have none),
# human-readable label (`.label`) and full description (`.description`), so
# consumers that need to show a code's meaning (e.g. form hydration/docs, or
# the dataset detail page's tooltip) don't need a separate reverse lookup
# against the vendored CSV or a live external API - one source of truth.


class DuoCodesEnum(Enum):
    def __new__(cls, code, shortcode, label, description):
        obj = object.__new__(cls)
        obj._value_ = code
        obj.shortcode = shortcode
        obj.label = label
        obj.description = description
        return obj

    DATA_USE_PERMISSION = (
        "DUO:0000001",
        "",
        "data use permission",
        "A data item that is used to indicate consent permissions for datasets "
        "and/or materials, and relates to the purposes for which datasets "
        "and/or material might be removed, stored or used.",
    )
    NRES = (
        "DUO:0000004",
        "NRES",
        "no restriction",
        "This data use permission indicates there is no restriction on use.",
    )
    HMB = (
        "DUO:0000006",
        "HMB",
        "health or medical or biomedical research",
        "This data use permission indicates that use is allowed for "
        "health/medical/biomedical purposes; does not include the study of "
        "population origins or ancestry.",
    )
    DS = (
        "DUO:0000007",
        "DS",
        "disease specific research",
        "This data use permission indicates that use is allowed provided it "
        "is related to the specified disease.",
    )
    POA = (
        "DUO:0000011",
        "POA",
        "population origins or ancestry research only",
        "This data use permission indicates that use of the data is limited "
        "to the study of population origins or ancestry.",
    )
    RS = (
        "DUO:0000012",
        "RS",
        "research specific restrictions",
        "This data use modifier indicates that use is limited to studies of "
        "a certain research type.",
    )
    NMDS = (
        "DUO:0000015",
        "NMDS",
        "no general methods research",
        "This data use modifier indicates that use does not allow methods "
        "development research (e.g., development of software or "
        "algorithms).",
    )
    GSO = (
        "DUO:0000016",
        "GSO",
        "genetic studies only",
        "This data use modifier indicates that use is limited to genetic "
        "studies only (i.e., studies that include genotype research alone "
        "or both genotype and phenotype research, but not phenotype "
        "research exclusively)",
    )
    DATA_USE_MODIFIER = (
        "DUO:0000017",
        "",
        "data use modifier",
        "Data use modifiers indicate additional conditions for use.",
    )
    NPUNCU = (
        "DUO:0000018",
        "NPUNCU",
        "not for profit, non commercial use only",
        "This data use modifier indicates that use of the data is limited "
        "to not-for-profit organizations and not-for-profit use, "
        "non-commercial use.",
    )
    PUB = (
        "DUO:0000019",
        "PUB",
        "publication required",
        "This data use modifier indicates that requestor agrees to make "
        "results of studies using the data available to the larger "
        "scientific community.",
    )
    COL = (
        "DUO:0000020",
        "COL",
        "collaboration required",
        "This data use modifier indicates that the requestor must agree to "
        "collaboration with the primary study investigator(s).",
    )
    IRB = (
        "DUO:0000021",
        "IRB",
        "ethics approval required",
        "This data use modifier indicates that the requestor must provide "
        "documentation of local IRB/ERB approval.",
    )
    GS = (
        "DUO:0000022",
        "GS",
        "geographical restriction",
        "This data use modifier indicates that use is limited to within a "
        "specific geographic region.",
    )
    MOR = (
        "DUO:0000024",
        "MOR",
        "publication moratorium",
        "This data use modifier indicates that requestor agrees not to "
        "publish results of studies until a specific date.",
    )
    TS = (
        "DUO:0000025",
        "TS",
        "time limit on use",
        "This data use modifier indicates that use is approved for a "
        "specific number of months.",
    )
    US = (
        "DUO:0000026",
        "US",
        "user specific restriction",
        "This data use modifier indicates that use is limited to use by "
        "approved users.",
    )
    PS = (
        "DUO:0000027",
        "PS",
        "project specific restriction",
        "This data use modifier indicates that use is limited to use "
        "within an approved project.",
    )
    IS = (
        "DUO:0000028",
        "IS",
        "institution specific restriction",
        "This data use modifier indicates that use is limited to use "
        "within an approved institution.",
    )
    RTN = (
        "DUO:0000029",
        "RTN",
        "return to database or resource",
        "This data use modifier indicates that the requestor must return "
        "derived/enriched data to the database/resource.",
    )
    GRU = (
        "DUO:0000042",
        "GRU",
        "general research use",
        "This data use permission indicates that use is allowed for "
        "general research use for any research purpose.",
    )
    CC = (
        "DUO:0000043",
        "CC",
        "clinical care use",
        "This data use modifier indicates that use is allowed for clinical "
        "use and care.",
    )
    NPOA = (
        "DUO:0000044",
        "NPOA",
        "population origins or ancestry research prohibited",
        "This data use modifier indicates use for purposes of population, "
        "origin, or ancestry research is prohibited.",
    )
    NPU = (
        "DUO:0000045",
        "NPU",
        "not for profit organisation use only",
        "This data use modifier indicates that use of the data is limited "
        "to not-for-profit organizations.",
    )
    NCU = (
        "DUO:0000046",
        "NCU",
        "non-commercial use only",
        "This data use modifier indicates that use of the data is limited "
        "to not-for-profit use.",
    )

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        schema = handler.resolve_ref_schema(handler(core_schema))
        schema.pop("enum", None)
        schema["type"] = "string"
        schema["oneOf"] = [
            {
                "const": m.value,
                "title": m.label,
                "shortcode": m.shortcode,
                "description": m.description,
            }
            for m in cls
        ]
        return schema
