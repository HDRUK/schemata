from hdr_schemata.models.annotations import get_annotations
import os

annotations = get_annotations(os.path.dirname(os.path.abspath(__file__)))
