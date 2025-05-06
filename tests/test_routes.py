import unittest
import json
from app import create_app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_get_empty_data(self):
        response = self.app.get('/api/data')
        self.assertEqual(response.status_code, 200)

    def test_post_valid_data(self):
        payload = {"name": "Test", "age": 25}
        response = self.app.post(
            '/api/data',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_post_invalid_data(self):
        response = self.app.post('/api/data', data="not json", content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
