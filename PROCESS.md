# Development Process Notes

Setup the directory/repository structure:

```sh
cd ~/Desktop
mkdir final-freestyle-project
cd final-freestyle-project
mkdir app
touch app/gas_prices_by_location.py
```

Set up a virtual environment and install packages:

```sh
pipenv install
pipenv install requests
pipenv install python-dotenv
#When dotenv is not able to be envoked, Bash is the alternative.
pipenv install ipython
```

Run the script:

```sh
pipenv shell
(my-freestyle-project) bash-3.2$ python app/gas_prices_by_location.py
```
