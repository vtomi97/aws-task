# open_meteo.py

import requests

class OpenMeteo:
    BASE_URL = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    def get_weather(self):
        #if params is None:
         #   params = {}
        #params['latitude'] = self.latitude
        #params['longitude'] = self.longitude
        response = requests.get(self.BASE_URL)
        #response.raise_for_status()
        return response.json()