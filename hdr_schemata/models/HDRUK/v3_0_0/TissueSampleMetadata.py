from hdr_schemata.models import remove_fields_from_cls
from hdr_schemata.models.HDRUK.v2_2_0.TissueSampleMetadata import TissueSampleMetadata as BaseTissueSampleMetadata

class TissueSampleMetadata(BaseTissuesSampleMetadata):
    pass

remove_fields_from_cls(TissueSampleMetadata, ["creationDate", "AnatomicalSiteOntologyCode"])