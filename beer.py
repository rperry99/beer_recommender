# Import Statements
import json
import requests
from random import randint

# Get user input, and run a query on the API using the input.
food_choice = input('Please enter your dinner choice: ')
url = f'https://api.punkapi.com/v2/beers?food={food_choice}'

r = requests.get(url)
data = json.loads(r.text)

# Create a recommended beer list array based on user input.
beer_list = []

for beer in data:
    name = beer['name']
    tagline = beer['tagline']
    abv = beer['abv']
    desc = beer['description']

    beer_item = {
        'name': name,
        'tagline': tagline,
        'abv': abv,
        'desc': desc
    }

    beer_list.append(beer_item)

# Generate a random recommendation from the beer list array
value = randint(0,len(beer_list))
recommendation = beer_list[value]

# Set each piece of the recommendation to it's own variable for nicer output.
rec_name = recommendation['name']
rec_tagline = recommendation['tagline']
rec_abv = recommendation['abv']
rec_desc = recommendation['desc']

# Display the recommended beer.
print("If you are ordering " + food_choice + ", then might we suggest " + rec_name + "." + " " + rec_tagline)
print(rec_desc)
print("The ABV is " + str(rec_abv) + ".")
