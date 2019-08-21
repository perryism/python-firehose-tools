import json, base64

class Record:
    def __init__(self, record):
        self.record = record

    def decoded_data(self):
        return base64.b64decode(self.record['data'])

    def merge(self, new_data):
        return {
            'recordId': self.record['recordId'],
            'result': 'Ok',
            'data': self.encode_data(new_data)
        }

    def encode_data(self, new_data):
        return base64.encodebytes(new_data.encode()).decode()
