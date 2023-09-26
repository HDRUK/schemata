from pydantic import ValidationError
import json

from hdr_schemata.models.HDRUK import Hdruk212
from hdr_schemata.models.GWDM import Gwdm10

def get_metadata(model,version):
    metadata = json.load(open(f'../examples/{model}/{version}/example.json'))
    return metadata

class TestHdruk212:
    metadata = get_metadata('HDRUK','2.1.2')

    def test_validation(self):
        assert Hdruk212(**self.metadata) != None

    def test_json_schema(self):
        schema = Hdruk212.model_json_schema()
        expected_keys = ['$defs', 'additionalProperties', 'properties', 'required', 'title', 'type']
        assert list(schema.keys()) == expected_keys

class TestGwdm10:
    metadata = get_metadata('GWDM','1.0')

    def test_validation(self):
        assert Gwdm10(**self.metadata) != None

    def test_json_schema(self):
        schema = Gwdm10.model_json_schema()
        expected_keys = ['$defs', 'additionalProperties', 'properties', 'required', 'title', 'type']
        assert list(schema.keys()) == expected_keys
