import time
import requests
import json
import os

def find_free_games():

    path = os.path.join(os.path.dirname(__file__), 'info.json')
    info = requests.get('https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=US&allowCountries=US').json()

    games = []
    elements = info['data']['Catalog']['searchStore']['elements']

    for game in elements:
        title = game.get('title', 'N/A')
        discount_price = game.get('price', {}).get('totalPrice', {}).get('discountPrice', 0) / 100
        
        games.append({
            'title': title,
            'price': discount_price
        })

    with open(path, 'w') as f:
        json.dump(games, f, indent=4)

find_free_games()