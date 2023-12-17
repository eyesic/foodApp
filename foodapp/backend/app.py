import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    user_location = request.args.get('location')
    term = 'food'
    api_key = 'oOPSmJXc-ReasQ3ujf3fJL1mbebm89JjtgwTjCcQ5A4CkRnl7_oyRLP746lkm7c0Own6G1AWHOeWNIlXUaTVPgJ10NQbQeVskDhLS2e01rz3zyGOnYtwwRviOzp-ZXYx'  # Ideally fetched from a secure environment variable
    headers = {'Authorization': f'Bearer {api_key}'}
    search_url = "https://api.yelp.com/v3/businesses/search"
    
    params = {
        'term': term,
        'location': user_location
    }
    
    response = requests.get(search_url, headers=headers, params=params)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()
