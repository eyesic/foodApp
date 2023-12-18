import json
import pytest
from unittest.mock import patch
from foodapp.backend.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_recommendations(client):
    response = client.get('/recommendations/manual?location=New+York')
    assert response.status_code == 200
    # Further checks can be added here to validate the response data

@patch('requests.get')
def test_auto_location_recommendations(mock_get, client):
    # Mock response for IPInfo
    mock_get.return_value.json.return_value = {
        'latitude': '40.7128',
        'longitude': '-74.0060'
    }

    response = client.get('/recommendations/auto')
    assert response.status_code == 200
    # Add more assertions as necessary

@patch('requests.get')
def test_manual_location_recommendations(mock_get, client):
    # Mock response for Yelp API
    mock_get.return_value.json.return_value = {
        'businesses': [
            {'name': 'Example Restaurant', 'rating': 4.5},
            # ... other mock businesses ...
        ]
    }

    response = client.get('/recommendations/manual?location=New+York')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert 'Example Restaurant' in data['businesses'][0]['name']
    # Add more assertions as necessary
