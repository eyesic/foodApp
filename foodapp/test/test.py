import unittest
from foodapp import app

class APITestCase(unittest.TestCase):

    def setUp(self):
        # Assuming 'app' is your Flask application
        self.client = app.test_client()
        
    def test_get_recommendations(self):
        # Send a GET request to the API
        response = self.client.get('/api/recommendations?location=New+York')
        self.assertEqual(response.status_code, 200)
        # Further checks can be added here to validate the response data

if __name__ == '__main__':
    unittest.main()

