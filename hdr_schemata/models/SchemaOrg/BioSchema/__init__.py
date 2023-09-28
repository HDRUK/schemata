import json
from pydantic import BaseModel, Field
from hdr_schemata.models.SchemaOrg.base import Dataset as BaseDataset

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

__fields_to_keep = [
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
]

# - There is a problem with pydantic v2 where the 'exclude' feature doesnt currently work
#   see: https://github.com/pydantic/pydantic/discussions/2686
# - This hack means that I can inherit from the Schema.Org model but then exclude fields
#   that are not needed for the BioSchema
all_keys = list(Dataset.model_fields.keys())
for field in all_keys:
    if not field in __fields_to_keep:
        if type(Dataset.__fields_set__) == set:
            Dataset.__fields_set__.remove(field)
        del Dataset.model_fields[field]

for field in __fields_to_keep:
    if not field in Dataset.model_fields.keys():
        raise NotImplementedError(f'Field "{field}" has not been implemented!')
