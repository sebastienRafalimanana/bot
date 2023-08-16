import datetime
import requests
from requests import Response
from config import Config


def get_pharmacy_request(code_region):
    response = requests.get(f"{Config.URL_API}{code_region}")
    pharmacies_data = response.json() if response.status_code == 200 else []
    return pharmacies_data