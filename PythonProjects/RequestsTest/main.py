"""
Kolorado test api
"""
import requests  

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    "Content-Type": "application/json",
    "Trainer-Token": "6d8a3d631ea1b0cfb01ac404bcbcaf36"
}

body = {
    
    "name": "Крошка",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"

}
# response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
# print(f'Статус код:{response.status_code}.Сообщение:{response.text}')

import requests  

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    "Content-Type": "application/json",
    "Trainer-Token": "6d8a3d631ea1b0cfb01ac404bcbcaf36"
}

body = {
    "pokemon_id": "28344",
    "name": "Картошка"
}
# response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
# print(f'Статус код:{response.status_code}.Сообщение:{response.text}')

import requests  

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    "Content-Type": "application/json",
    "Trainer-Token": "6d8a3d631ea1b0cfb01ac404bcbcaf36"
}

body = {
    "pokemon_id": "28350"
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(f'Статус код:{response.status_code}.Сообщение:{response.text}')