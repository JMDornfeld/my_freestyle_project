from app.gas_prices_by_location import enlarge, parse_response

def test_enlarge():
    result = enlarge(3)
    assert result == 300

import csv
import json
import os
import pdb

def test_parse_response():
    # setup:
    json_filepath = os.path.join(os.path.dirname(__file__), "gas_prices.json")
    with open(json_filepath, "r") as json_file: # h/t: https://stackoverflow.com/a/2835672/670433
        raw_response = json.load(json_file)
    # test:

    parsed_response = parse_response(raw_response)
    test_response = [{
    		"zip": "10009",
    		"reg_price": "N\/A",
    		"mid_price": "N\/A",
    		"pre_price": "4.94",
    		"diesel_price": "N\/A",
    		"address": "253 E 2nd St",
    		"diesel": "1",
    		"lat": "40.721119",
    		"lng": "-73.981308",
    		"station": "Mobil",
    		"city": "New York",
    		"distance": "0.8 miles"
    	}, {
    		"zip": "11101",
    		"reg_price": "N\/A",
    		"mid_price": "N\/A",
    		"pre_price": "N\/A",
    		"diesel_price": "3.91",
    		"address": "2701 Jackson Ave",
    		"diesel": "1",
    		"lat": "40.747738",
    		"lng": "-73.940712",
    		"station": "Gulf",
    		"city": "Long Island City",
    		"distance": "2.7 miles"
    	}]
    assert parsed_response == test_response
