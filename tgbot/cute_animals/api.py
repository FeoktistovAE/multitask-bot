import requests
import json
from tgbot.config import load_config


config = load_config(".env")
animal_pictures_token = config.misc.animal_pictures_token

URL = "https://api.unsplash.com/photos/random"

'''Заголовок, необходимый для авторизации'''
headers = {
        "Authorization": f"Client-ID {animal_pictures_token}"
    }

'''ID коллекции фотографий милых животных сервиса unsplash'''
params = {
    'collections': '1489913',
}


def get_animal_url() -> str:
    response = requests.get(URL, headers=headers, params=params)
    return json.loads(response.content)["urls"]["regular"]
