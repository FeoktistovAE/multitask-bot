from tgbot.config import load_config
import requests


config = load_config(".env")

payload = {}
headers = {
"apikey": config.misc.exchange_rates_token
}

def get_convertation_data(to_currency: str, from_currency: str, amount: str):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    
    return requests.request("GET", url, headers=headers, data=payload).content
