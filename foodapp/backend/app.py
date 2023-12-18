import os
import requests
from flask import Flask, request, jsonify
import ipinfo

# Use environment variables for sensitive data like API keys
YELP_API_KEY = os.environ.get('YELP_API_KEY')
IPINFO_ACCESS_TOKEN = os.environ.get('IPINFO_ACCESS_TOKEN')

def get_yelp_recommendations(latitude, longitude):
    headers = {'Authorization': f'Bearer {YELP_API_KEY}'}
    search_url = "https://api.yelp.com/v3/businesses/search"
    params = {'latitude': latitude, 'longitude': longitude, 'categories': 'food', 'limit': 10}

    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        # Log the error or return a more descriptive error message
        return {'error': 'Unable to fetch data from Yelp', 'status_code': response.status_code}

def get_yelp_recommendations_by_location(location):
    headers = {'Authorization': f'Bearer {YELP_API_KEY}'}
    search_url = "https://api.yelp.com/v3/businesses/search"
    params = {'location': location, 'categories': 'food', 'limit': 10}

    response = requests.get(search_url, headers=headers, params=params)
    return response.json()

app = Flask(__name__)
handler = ipinfo.getHandler(IPINFO_ACCESS_TOKEN)

@app.route('/')
def index():
    return "Welcome to the foodAPI"

@app.route('/recommendations/manual')
def manual_location_recommendations():
    user_input_location = request.args.get('location')
    recommendations = get_yelp_recommendations_by_location(user_input_location)
    return jsonify(recommendations)

@app.route('/recommendations/auto')
def auto_location_recommendations():
    ip_address = request.remote_addr
    details = handler.getDetails(ip_address)

    # Check if latitude and longitude are available
    latitude = getattr(details, 'latitude', None)
    longitude = getattr(details, 'longitude', None)

    if latitude and longitude:
        recommendations = get_yelp_recommendations(latitude, longitude)
        return jsonify(recommendations)
    else:
        return jsonify({'error': 'Location details not available for the IP address'})

if __name__ == '__main__':
    app.run()
