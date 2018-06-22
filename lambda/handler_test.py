import unittest
import json

from handler import handler


class HandlerTest(unittest.TestCase):
    def test_handler(self):
        result = handler({
            'queryStringParameters': {}
        }, None)
        self.assertEqual(result['statusCode'], 400)
        self.assertEqual(result['body'], None)

        result = handler({
            'queryStringParameters': {
                'text': "fancy crimson lipstick"
            }
        }, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body'], json.dumps(['fan-cy', 'crim-son', 'lip-stick']))

        result = handler({
            'queryStringParameters': {
                'text': 123
            }
        }, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body'], json.dumps(['123']))
