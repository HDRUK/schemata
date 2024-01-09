from hdr_schemata.models.HDRUK.v2_1_2 import Provenance as BaseProvenance
from .Temporal import Temporal


class Provenance(BaseProvenance):
    temporal: Temporal
