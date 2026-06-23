import os

from hdr_schemata.models.annotations import get_annotations
from hdr_schemata.models.HDRUK.v4_0_0.annotations import annotations

annotations = get_annotations(os.path.dirname(os.path.abspath(__file__)), annotations)
