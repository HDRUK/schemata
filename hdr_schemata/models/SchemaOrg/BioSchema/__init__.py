import json
from pydantic import BaseModel, Field
from hdr_schemata.models.SchemaOrg.base import Dataset as BaseDataset
from hdr_schemata.models import filter_fields_in_cls

class Dataset(BaseDataset):
    m_dct_conformsTo: dict = Field(
        alias="dct:conformsTo",
        default={
            "http://purl.org/dc/terms/conformsTo": {
                "@id": "https://bioschemas.org/profiles/Dataset/1.1-DRAFT",
                "@type": "CreativeWork"
            }
        }
    )

filter_fields_in_cls(Dataset,
                       [
                           "m_type",
                           "m_id",
                           "m_context",
                           "m_dct_conformsTo",
                           "description",
                           "identifier",
                           "keywords",
                           "license",
                           "name",
                           "url",
                           "alternateName",
                           "citation",
                           "creator",
                           "distribution",
                           "includedInDataCatalog",
                           "isBasedOn",
                           "measurementTechnique",
                           "sameAs",
                           "variableMeasured",
                           "version",
                           "dateCreated",
                           "dateModified",
                           "datePublished",
                           "hasPart",
                           "isAccessibleForFree",
                           "isPartOf",
                           "maintainer",
                           "publisher"
                       ])
