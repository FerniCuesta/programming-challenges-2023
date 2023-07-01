"""
Español

Implementa una llamada HTTP a una API y muestra su resultado a través de la terminal.

Aquí tienes un listado de posibles APIs: https://github.com/public-apis/public-apis

En mi caso, he usado una API de Pokemon para listar los n primeros Pokemon junto a sus habilidades
Se puede cambiar la cantidad de Pokemon listados modificando la constante 'NUMBER'
---------------------------------------------------------------------------------------------------
English

Implement a HTTP call to an API and show its result throught terminal.

Here you have a list of possible APIs: https://github.com/public-apis/public-apis

I used a Pokemon API to list the first n Pokemon with their abilities
The number of Pokemon listed can be changed by modifiyng the constan 'NUMBER'
"""

import requests

NUMBER = 50  # number of Pokemon to list
URL = f"https://pokeapi.co/api/v2/pokemon?limit={NUMBER}"

response_url = requests.get(URL, timeout=10)

for pokemon in response_url.json()["results"]:
    print("\n-------------------------------------")
    print("Pokemon:", pokemon["name"])

    url = pokemon["url"]
    response_pokemon = requests.get(url, timeout=10)

    print("Abilities slot:")
    for ability in response_pokemon.json()["abilities"]:
        print("\t", ability["slot"], ability["ability"]["name"])
