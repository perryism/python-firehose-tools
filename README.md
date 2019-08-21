# Overview

I just want to focus on transforming data from firehose, but there are so much time I am spending on decode the data from the stream and encode it back to the stream.  Therefore, I made this package to help me facilitate transformation


## Example

<pre>
from fhtools import Firehose

def lambda_handler(event, context):
    firehose = Firehose(event)

		@firehose.transform
    def transform(decoded_json_data):
        # do transformation here
        return new_decoded_json_data

    return firehose.map(transform)

</pre>
