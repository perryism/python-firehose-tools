import json, base64
from .record import Record

class JsonRecord(Record):
    def decoded_data(self):
        return json.loads(super().decoded_data())

    def encode_data(self, new_data):
        data = json.dumps(new_data)
        return super().encode_data(data)
