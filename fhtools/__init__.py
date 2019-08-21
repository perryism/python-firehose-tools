from .json_record import JsonRecord

class Firehose:
    def __init__(self, event, datatype=JsonRecord):
        self.event = event
        self.datatype = datatype

    def map(self, func):
        results = []
        for record in self.event['records']:
            transformed = func(record)
            if transformed:
                results.append(transformed)
        return {'records': results}

    def transform(self, func):
        def wrapper(record):
            jrecord = self.datatype(record)
            raw_payload = func(jrecord.decoded_data())
            return jrecord.merge(raw_payload)
        return wrapper
