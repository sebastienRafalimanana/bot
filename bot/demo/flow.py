from .external_request import get_weather, get_long_term_forecast
from flask import request
import requests
import datetime


def talk_weather(city):
    response = get_weather(city)
    data = response.json()
    if data["cod"] == "404":
        return "Ville non trouvée. Veuillez vérifier le nom de la ville."
    else:
        weather_id = data["weather"][0]["description"]
        weather_data = weather_descriptions_fr.get(weather_id, "condition météorologique inconnue")
        temperature = data["main"]["temp"]
        return f"La météo à {city.capitalize()} est : {weather_data}, Température : {temperature}°C"


def get_long_term_forecast(city):
    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=7)
    api_key = "ee2949f7a6d0f4b2fdb68421b49f6fca"
    base_url = "http://api.openweathermap.org/data/2.5/forecast/daily?"
    complete_url = f"{base_url}q={city}&appid={api_key}&cnt=7"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] == "404":
        return "Ville non trouvée. Veuillez vérifier le nom de la ville."
    else:
        forecast_data = data["list"]
        forecast_text = "Prévisions pour la semaine prochaine : \n"
        for forecast in forecast_data[1:]:
            date_str = datetime.datetime.fromtimestamp(forecast["dt"]).strftime("%Y-%m-%d")
            weather_id = forecast["weather"][0]["description"]
            weather_data = weather_descriptions_fr.get(weather_id, "condition météorologique inconnue")
            forecast_text += f"{date_str}: {weather_data}\n"
        return forecast_text


meteo_command_processed = {}


def handle_weather_command(message_text):
    global meteo_command_processed
    message_parts = message_text.split(" ", 1)
    command = message_parts[0].lower()

    if command == "meteo":
        sender_id = request.json["entry"][0]["messaging"][0]["sender"]["id"]
        if sender_id not in meteo_command_processed:
            meteo_command_processed[sender_id] = False

        if not meteo_command_processed[sender_id]:
            meteo_command_processed[sender_id] = True
            return "Veuillez saisir le nom de la ville pour connaître la météo."
        else:
            meteo_command_processed[sender_id] = False  # Réinitialiser l'état de traitement pour la prochaine fois
            if len(message_parts) > 1:
                city = message_parts[1]
                return talk_weather(city)
            else:
                return "Veuillez spécifier une ville pour obtenir la météo."
    elif command == "previsions":
        if len(message_parts) > 1:
            city = message_parts[1]
            return get_long_term_forecast(city)
        else:
            return "Veuillez spécifier une ville pour obtenir les prévisions à long terme."
    else:
        return "Commande non reconnue. Utilisez 'meteo [ville]' ou 'previsions [ville]'."


# Traduction description Fr
weather_descriptions_fr = {
    "clear sky": "ciel dégagé",
    "few clouds": "quelques nuages",
    "scattered clouds": "nuages épars",
    "broken clouds": "nuages épars",
    "shower rain": "averses de pluie",
    "rain": "pluie",
    "thunderstorm": "orage",
    "snow": "neige",
    "mist": "brume",
}
