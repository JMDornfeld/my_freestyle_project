# Project Planning
Jaclyn Dornfeld and Vincent Hamalainen will be working together

# Primary User
Cost conscious drivers

# User Needs Statement
As a cost conscious driver, I need a quicker way to find the cheapest gas near me or on my designated route. It would also be nice if the program could know where I am without me having to provide a lot of information.

# Existing Capabilities
Currently, I can use applications to help find the closest gas station on a mass scale (such as waze or google maps) but this application is designed purely based on location and price in real time.

# As-Is Process Description

Option 1
 1.      Plan out trip route prior to leaving
 2.      Research best priced and convenient gas stations
 3.      Incorporate gas stops into route
 4.      Leave for the trip

Option 2
 1.      Start trip
 2.      Decide that I need gas
 3A. Use google maps / waze (or current route calculating app of choice) to find the nearest gas station
 3B. Use the road signs to find the nearest gas station without price information
 
# To-Be Process Description
 
1.      User goes our new app (name TBD) and inputs their desired radius and fuel type
2.      Application provides gas stations nearby based on cost
3.      User selects best gas station for their route
4.      End state vision: Google Maps pulls up the best (a component of the added complexity for a two person project) 

# Information Requirements

# Information Inputs
1.      We will leverage the myGAS API key: http://www.mygasfeed.com/keys/api to provide the information surrounding gas prices and location
2.      We will leverage a location API key to provide information around the users current location without them having to input it. 
The data format of these inputs are the following arguments:
    latitude
   longitude
    distance
    fuel time
    sort by
   callback
3.      Additional location adjustment API to calculate zip code or address into latitude / longitude to coordinate with myGAS API

# Information Outputs

1.      Results of nearest gas station by cost (potentially printable version for user to take on mobile devise or printer)
# Technology Requirements

APIs and Web Service Requirements

1.      We will use the following API key for gas prices: http://www.mygasfeed.com/keys/api
2.      Additional location API (TBD)

# Python Package Requirements
This application requires the requests package to issue HTTP requests to that API. pytest is also required for for testing purposes.
Planning to leverage two API keys, dotenv or the bash application would be required to ensure API key privacy.

# Hardware Requirements:
No hardware requirements are necessary at this time. In the future, this application could be deployed to a public server but that is not in the scope of this initial project.
