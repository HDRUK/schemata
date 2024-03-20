from hdr_schemata.models.annotations import get_annotations
from hdr_schemata.models.HDRUK.v2_2_0.annotations import annotations
import os

annotations = get_annotations(os.path.dirname(os.path.abspath(__file__)), annotations)
