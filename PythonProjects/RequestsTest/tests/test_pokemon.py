import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = "94d5b17e3b4ad2632220d481bba655c3"
TRAINER_ID = 11700


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response.status_code == 200



@pytest.mark.parametrize('key, value', [('trainer_name', 'Myles')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
