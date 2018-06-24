# Gas Prices By Location

A command-line Python application which processes user inputs, user geo location and the mygas prices API from the [IP STACK API](http://api.ipstack.com/) and [MYGAS API] (http://api.mygasfeed.com/stations/radius/) to provide the best gas station option based on price and distance and to read the users location based on the computers location.

## Installation

First, "fork" [this upstream repository](https://github.com/prof-rossetti/nyu-info-2335-201805/blob/master/projects/freestyle/project.md) under your own control.

Then download your forked version of this repository using the GitHub.com online interface or the Git command-line interface. If you are using command-line Git, you can download it by "cloning" it:

```sh
git clone https://github.com/JMDornfeld/my_freestyle_project
```

After downloading your forked repository, navigate into its root directory:

```sh
cd final_prices_by_location-py/
```

> NOTE: all commands in this document assume you are running them from this root directory.

Install package dependencies using one of the following commands, depending on how you have installed Python and how you are managing packages:

```sh
# Pipenv on Mac or Windows:
pipenv install -r requirements.txt

# Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt

# All others:
pip install -r requirements.txt
```

## Setup

Obtain an [IP STACK API](http://api.ipstack.com/) and [MYGAS API](https://www.alphavantage.co/support/#api-key), which the app will supply when issuing requests to the API.

To prevent your secret API Key from being tracked in version control, the application looks for an environment variable named `MYGAS_API_KEY` and `GEO_API_Key`. To set this environment variable, create a new file in this directory called ".env" and place inside the following contents:

    MYGAS_API_KEY="type_api_key_here" # use your own API Key instead of "type_api_key_here"
    GEO_API_Key="type_api_key_here" # use your own API Key instead of "type_api_key_here"

## Usage

If you are using Pipenv, enter a new virtual environment (`pipenv shell`) before running any of the commands below.

Run the recommendation script:

```sh
# Homebrew-installed Python 3.x on Mac OS, not using Pipenv:
python3 app/final_prices_by_location.py

# All others, including Pipenv on Mac or Windows:
python app/final_prices_by_location.py
```

## [License](LICENSE.md)

Please read the License document for API regulations and best practices following the instructions above in "setup".
