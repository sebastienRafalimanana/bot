
import datetime
from flask import request, Blueprint
from pymessenger.bot import Bot
import requests

wealther = Blueprint("wealther", __name__)
ACCESS_TOKEN = 'EAAECHxkNCc0BOzmWOGwj7xMmBITos0AMMOXlxRe4pVl2VNY3FzjvwvnYXVZCeefJiFOg95P3uhjYgu6ZAvZCx74VpsWVNbk8fjVmaHUsL7SBZCJsefjefpZB6P161fHazkmghQGe5ojJZArnKJL9RmauK80I5GyBwBwQNP6QHFVMAF4vCcXoZCaX7Ktp9H3LXii'
VERIFY_TOKEN = '2kl73mjy1e'
bot = Bot(ACCESS_TOKEN)

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

#We will receive messages that Facebook sends our bot at this endpoint
@wealther.route("/wealther", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Verification token"""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       print(output)
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
              if message.get('message'):
                  recipient_id = message['sender']['id']
                  message_text = message['message'].get('text', '').lower()
                  response_sent_text = handle_weather_command(message_text)
                  send_message(recipient_id, response_sent_text)
    return "Message Processed"



def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"
def get_weather(city):
    api_key = "ee2949f7a6d0f4b2fdb68421b49f6fca"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"  # units=metric pour obtenir la température en Celsius
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] == "404":
        return "Ville non trouvée. Veuillez vérifier le nom de la ville."
    else:
        #weather_data = data["weather"][0]["description"]
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
                return get_weather(city)
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


