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
    desc = beer['description']

    beer_item = {
        'name': name,
        'tagline': tagline,
        'abv': abv,
        'desc': desc
    }

    beer_list.append(beer_item)

value = randint(0,len(beer_list))

recommendation = beer_list[value]

rec_name = recommendation['name']
rec_tagline = recommendation['tagline']
rec_abv = recommendation['abv']
rec_desc = recommendation['desc']

print("If you are ordering " + food_choice + ", then might we suggest " + rec_name + "." + " " + rec_tagline)
print(rec_desc)
print("The ABV is " + str(rec_abv) + ".")
