import requests

def get_yelp_recommendations(latitude, longitude):
    yelp_api_key = 'oOPSmJXc-ReasQ3ujf3fJL1mbebm89JjtgwTjCcQ5A4CkRnl7_oyRLP746lkm7c0Own6G1AWHOeWNIlXUaTVPgJ10NQbQeVskDhLS2e01rz3zyGOnYtwwRviOzp-ZXYx'  # Replace with your actual Yelp API key
    headers = {'Authorization': f'Bearer {yelp_api_key}'}
    search_url = "https://api.yelp.com/v3/businesses/search"
    
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'categories': 'food',  # Assuming you want to search for food-related businesses
        'limit': 10  # Limit the number of results
    }

    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()  # Return the JSON response from Yelp API
    else:
        return {'error': 'Unable to fetch data from Yelp'}  # Handle potential errors
    

def get_yelp_recommendations_by_location(location):
    yelp_api_key = 'oOPSmJXc-ReasQ3ujf3fJL1mbebm89JjtgwTjCcQ5A4CkRnl7_oyRLP746lkm7c0Own6G1AWHOeWNIlXUaTVPgJ10NQbQeVskDhLS2e01rz3zyGOnYtwwRviOzp-ZXYx'  
    headers = {'Authorization': f'Bearer {yelp_api_key}'}
    search_url = "https://api.yelp.com/v3/businesses/search"
    params = {'location': location, 'categories': 'food', 'limit': 10}

    response = requests.get(search_url, headers=headers, params=params)
    return response.json()
