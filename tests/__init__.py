import unittest
import json, base64
from fhtools import Firehose

class TestFirehoseTools(unittest.TestCase):
    def setUp(self):
        with open("tests/fixtures/firehose_event.json", "r") as f:
            self.event = json.loads(f.read())

    def test_function_injection(self):
        f = Firehose(self.event)

        @f.transform
        def transform(record):
            self.assertEqual(record, {"foo": "bar"})
            return record

        f.map(transform)

    def test_transform(self):
        f = Firehose(self.event)

        @f.transform
        def transform(record):
            record["bar"] = "foo"
            return record

        decoded_data = json.loads(base64.b64decode(self.event["records"][0]["data"]))
        self.assertEqual(decoded_data, {"foo": "bar"})
        results = f.map(transform)
        decoded_data = base64.b64decode(results["records"][0]["data"])
        self.assertEqual(decoded_data, b'{"foo": "bar", "bar": "foo"}')
