import json
import requests
from pprint import pprint

url = 'https://superheroapi.com/api/2619421814940190/search/'
headers = {'Autorization': '2619421814940190'}

heroes = ['Hulk', 'Captain America', 'Thanos']

intelligence_heroes = {}

def superheroes(url, search_hero, headers):
    for item in range(len(search_hero)):
        resp = requests.get(url + search_hero[item], headers = headers)
        url_dict = resp.json()
        powerstats = url_dict['results'][0]
        for search in powerstats.items():
            for hero in search:
                if 'intelligence' in hero:
                    intelligence_heroes[search_hero[item]] = int(hero['intelligence'])
    smart_hero = max(intelligence_heroes, key = intelligence_heroes.get)
    pprint(smart_hero)

if __name__ == '__main__':
    superheroes(url, heroes, headers)



