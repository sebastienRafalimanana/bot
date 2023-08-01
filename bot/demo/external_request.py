import datetime
import requests
from requests import Response


def get_weather(city):
    api_key = "ee2949f7a6d0f4b2fdb68421b49f6fca"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response: Response = requests.get(complete_url)
    return response


def get_long_term_forecast(city):
    today = datetime.date.today()
    api_key = "ee2949f7a6d0f4b2fdb68421b49f6fca"
    base_url = "http://api.openweathermap.org/data/2.5/forecast/daily?"
    complete_url = f"{base_url}q={city}&appid={api_key}&cnt=7"
    response: Response = requests.get(complete_url)
    return response
