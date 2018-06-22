import pyphen
import json


def handler(event, context):
    queryStringParameters = event['queryStringParameters']

    if 'word' not in queryStringParameters:
        return {
            'statusCode': 400,
            'body': None
        }

    dic = pyphen.Pyphen(lang="en_US")
    return {
        'statusCode': 200,
        'body': json.dumps(
            dic.inserted(queryStringParameters['word'])
        )
    }
