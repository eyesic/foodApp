
from flask import Flask, request, jsonify
import ipinfo
from foodapp.backend import get_yelp_recommendations_by_location, get_yelp_recommendations

app = Flask(__name__)

access_token = 'ca9af5c4faddf4'
handler = ipinfo.getHandler(access_token)

@app.route('/')
def index():
    return "Welcome to the foodAPI"

@app.route('/recommendations/manual')
def manual_location_recommendations():
    user_input_location = request.args.get('location')

    # Use the Yelp API to get recommendations based on the user's input
    recommendations = get_yelp_recommendations_by_location(user_input_location)
    return jsonify(recommendations)



# Grabs ip and then 
@app.route('/recommendations/auto')
def auto_location_recommendations():
    ip_address = request.remote_addr
    details = handler.getDetails(ip_address)

    latitude = details.latitude
    longitude = details.longitude

    recommendations = get_yelp_recommendations(latitude, longitude)
    return jsonify(recommendations)



if __name__ == '__main__':
    app.run()
