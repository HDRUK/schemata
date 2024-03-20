from hdr_schemata.models.annotations import annotations, get_annotations
import os

# print(annotations.Common.provenance.__dict__.keys())

annotations = get_annotations(
    os.path.dirname(os.path.abspath(__file__)), annotations.Common
)


# print(annotations.provenance.origin.__dict__.keys())
