import json
import requests
from random import randint

food_choice = input('Please enter your dinner choice: ')
url = f'https://api.punkapi.com/v2/beers?food={food_choice}'

r = requests.get(url)
data = json.loads(r.text)

beer_list = []

for beer in data:
    name = beer['name']
    tagline = beer['tagline']
    abv = beer['abv']

    beer_item = {
        'name': name,
        'tagline': tagline,
        'abv': abv
    }

    beer_list.append(beer_item)

value = randint(0,len(beer_list))

recommendation = beer_list[value]

rec_name = recommendation['name']
rec_tagline = recommendation['tagline']
rec_abv = recommendation['abv']

print("If you are ordering " + food_choice + ", then might we suggest " + rec_name + ".")
print("It is a \"" + rec_tagline + "\".")
print("The ABV is " + str(rec_abv) + ".")
