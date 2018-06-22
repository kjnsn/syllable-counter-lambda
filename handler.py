import imp
import sys
sys.modules["sqlite"] = imp.new_module("sqlite")
sys.modules["sqlite3.dbapi2"] = imp.new_module("sqlite.dbapi2")
import nltk
nltk.data.path.append("/var/task/nltk_data")

import pyphen
import json
from textblob import TextBlob


def handler(event, context):
    """Handles the event from lambda"""

    query_string_parameters = event['queryStringParameters']

    if 'text' not in query_string_parameters:
        return {
            'statusCode': 400,
            'body': None
        }

    # Extract the words from the text.
    blob = TextBlob(str(query_string_parameters['text']))

    dic = pyphen.Pyphen(lang="en_US")
    return {
        'statusCode': 200,
        'body': json.dumps(
            list(map(dic.inserted, blob.words))
        )
    }
