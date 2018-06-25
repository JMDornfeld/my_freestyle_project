import os
import json
import requests
import datetime
#import pdb
import webbrowser

#more details here http://www.mygasfeed.com/keys/api
#Get Nearby Gas Stations
#http://api.mygasfeed.com/stations/radius/(Latitude)/(Longitude)/(distance)/(fuel type)/(sort by)/apikey.json?callback=?
#Gas Price History
#http://api.mygasfeed.com/locations/pricehistory/(station id)/apikey.json?callback=?
#Gas Station Brands
#http://api.mygasfeed.com/stations/brands/apikey.json?callback=?
#Gas Station Details
#http://api.mygasfeed.com/stations/details/(Stattion Id)/apikey.json?callback=?

mygas_api_key = os.environ.get("MYGAS_API_KEY")
GEO_API_Key = os.environ.get("GEO_API_Key")

def parse_response(response_text):
    if isinstance(response_text, str):
        response_text = json.loads(response_text)

    #pdb.set_trace()

    results = []
    stations = response_text["stations"]
    for stat in stations:
        #pdb.set_trace()
        result = {
            #"country": stat["country"],
            "reg": stat["reg_price"],
            "mid": stat["mid_price"],
            "pre": stat["pre_price"],
            "diesel": stat["diesel_price"],
            "address": stat["address"],
            "diesel": stat["diesel"],
            #"id": stat["id"],
            "lat": stat["lat"],
            "lng": stat["lng"],
            "station": stat["station"],
            #"region": stat["region"],
            "city": stat["city"],
            #"reg_date": stat["reg_date"],
            #"mid_date": stat["mid_date"],
            #"pre_date": stat["pre_date"],
            #"diesel_date": stat["diesel_date"],
            "distance": stat["distance"]
        }
        results.append(result)
    return results

send_url = f'http://api.ipstack.com/check?access_key={GEO_API_Key}'
r = requests.get(send_url)
j = json.loads(r.text)
latitude = j['latitude']
longitude = j['longitude']

while True:
    distance = input("Please enter desired radius in miles:     ")
    if distance.isalpha():
        print ("Invalid Distance. Please try again")
    elif int(distance) > 50:
       print ("Distance too large. Please try again")
    else:
        break

while True:
    fuel_type = input("Please enter your prefered fuel type using reg, mid, pre or diesel:    ")
    if fuel_type == "reg" or fuel_type == "mid" or fuel_type == "pre" or fuel_type == "diesel":
        break
    else:
        print ("Invalid Fuel Type. Please try again")
sort_by = "price"

request_url = f"http://api.mygasfeed.com/stations/radius/{latitude}/{longitude}/{distance}/{fuel_type}/{sort_by}/{mygas_api_key}.json?"

response = requests.get(request_url)

if "Request ok" not in response.text:
    print("REQUEST ERROR, PLEASE TRY AGAIN. CHECK YOUR INPUTS.  ")
    quit("Stopping the program")

station_prices = parse_response(response.text)

#this list comprehension removes all "N/A" values from our list based on fuel_type selected
station_prices = [d for d in station_prices if d[fuel_type] != "N/A"]

print("------------------------------------")
print("Date & Time the program was executed: ", datetime.datetime.now().strftime("%m-%d-%y %H:%M"))
print("Listing the three cheapest gas stations in your selected distance:")
print("GAS STATION #1:    ")
print("PRICE:  " + '${0:.2f}'.format(float(station_prices[0][fuel_type])))
print("DISTANCE:  " + station_prices[0]["distance"])
print("ADDRESS:  " + station_prices[0]["address"])
print("GAS STATION #2:    ")
print("PRICE:  " + '${0:.2f}'.format(float(station_prices[0][fuel_type])))
print("DISTANCE:  " + station_prices[1]["distance"])
print("ADDRESS:  " + station_prices[1]["address"])
print("GAS STATION #3:    ")
print("PRICE:  " + '${0:.2f}'.format(float(station_prices[0][fuel_type])))
print("DISTANCE:  " + station_prices[2]["distance"])
print("ADDRESS:  " + station_prices[2]["address"])
print("------------------------------------")
while True:
    station_choice = input("Which station would you like to navigate to? (please enter the number):     ")
    if station_choice.isalpha():
        print("Selection Invalid.")
    elif station_choice != "1" and station_choice != "2" and station_choice != "3":
        print("Selection Invalid.")
    else:
        break
station_choice = int(station_choice)-1
a = station_prices[station_choice]["lat"]
b = station_prices[station_choice]["lng"]
final_url = f"https://www.google.com/maps/dir/?api=1&origin={latitude},{longitude}&destination={a},{b}&travelmode=driving"
webbrowser.open(final_url, new=2)

def enlarge(i):
    return i * 100
