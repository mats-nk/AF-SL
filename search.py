#!/bin/python
import requests
import json
import sys
import re
import time
from geopy.geocoders import Nominatim

"""
Install python packages:
   pip install -r requirements.txt

Add your api-key to filename
Add the url to the system you are running the tests against
Add a argument as search term
"""

url = "https://jobsearch.api.jobtechdev.se/search"
filename = 'apikey'

geolocator = Nominatim(user_agent="Arbetsformedlingen-Adr")

def get_file_contents(filename):
    try:                           # It's assumed our file contains a single line, with our API key
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)


def test_search_return_number_of_hits(query):
    limit = 0                      # Limit: 0 means no ads, just a value of how many ads were found
    search_params = {'q': query, 'limit': '0'}
    response = requests.get(url, headers=headers, params=search_params)
    response.raise_for_status()    # Check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    number_of_hits = json_response['total']['value']


def test_search_loop_through_hits(query):
    limit = 100                    # 100 is max number of hits that can be returned.
                                   # If there are more (which you find with 'limit' : 0 ) you have
                                   # to use offset and multiple requests to get all ads
    search_params = {'q': query, 'limit': limit}
    response = requests.get(url, headers=headers, params=search_params)
    response.raise_for_status()    # Check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    hits = json_response['hits']
    with open(query + '-search.json', "w") as outfile:
        json.dump(json_response, outfile)
    for hit in hits:
        print()
        print(hit['headline'])
        print(hit['webpage_url'])

        # OBS AF skickar ut
        # - long, lat
        # men geolocator vill ha
        # - lat, long

        #print(type(hit['workplace_address']['coordinates']))
        cord = hit['workplace_address']['coordinates']
        print(type(cord))
        #lat=cord[1]
        #lon=cord[0]
        cord = cord.reverse()
        print(cord)
        #location = geolocator.reverse(cord)
        #print(location)
        print('')

        print(hit['workplace_address']['street_address'])
        #print(hit['workplace_address']['postcode'])
        #print(hit['workplace_address']['city'])

        print('')
        #time.sleep(1)


# ------ Main ------
if __name__ == '__main__':
    api_key = get_file_contents(filename)

    headers = {'api-key': api_key, 'accept': 'application/json'}

    test_search_return_number_of_hits(sys.argv[1])

    test_search_loop_through_hits(sys.argv[1])

