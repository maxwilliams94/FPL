import requests

api_static = "https://fantasy.premierleague.com/api/bootstrap-static/"

response = requests.get(api_static)

# type(data) : dict
data = response.json()


# type(data['events']) list
events = data['events']
# list of dictionaries
