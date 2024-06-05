from hdr_schemata.models.HDRUK.v2_2_0 import TissuesSampleCollection as BaseTissuesSampleCollection
from hdr_schemata.models import remove_fields_from_cls


class TissuesSampleCollection(BaseTissuesSampleCollection):
    pass

remove_fields_from_cls(TissuesSampleCollection, [
    "dataCategories", "collectionType","materialType"
])
