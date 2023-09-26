from pydantic import ValidationError
import v1_0
import json


metadata = json.load(open('1.0/example.json'))

try:
    v1_0.Gwdm10(**metadata)
    v1_0.Gwdm10.save_schema()
except ValidationError as e:
    print(e)


