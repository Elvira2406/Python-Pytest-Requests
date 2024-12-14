import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = "94d5b17e3b4ad2632220d481bba655c3"
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token': TOKEN
}

body_pokemon= {
    "name": "Бульбазавр",
    "photo_id": 1
}



response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon)
print(response_create.text)

pokemon_id = response_create.json()['id']

print(pokemon_id)

body_change = {
    "pokemon_id": pokemon_id,
    "name": "Lola",
    "photo_id": 24
}

body_pokeball = {
    "pokemon_id": pokemon_id
}


response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_change)
print(response_add_pokeball.text)
