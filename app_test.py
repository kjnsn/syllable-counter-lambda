import unittest
import json

from app import app


class HandlerTest(unittest.TestCase):
    def test_handler(self):
        with app.test_client() as c:
            rv = c.get('/')
            json_data = rv.get_json()
            self.assertEqual(json_data, [])

            rv = c.get('/?text=fancy+crimson+lipstick')
            json_data = rv.get_json()
            self.assertEqual(json_data, ['fan-cy', 'crim-son', 'lip-stick'])

            rv = c.get('/?text=123')
            json_data = rv.get_json()
            self.assertEqual(json_data, ['123'])
