import requests


class CSGOMarket:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://market.csgo.com/api/v2/'

    def get_weapon_price(self, weapon_name: str, rate='RUB'):
        rate_add = f'prices/{rate}.json'
        response = requests.get(self.base_url + rate_add)
        data = response.json()
        for weapon in data['items']:
            if weapon['market_hash_name'] == weapon_name:
                return weapon
        return None



