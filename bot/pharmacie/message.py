import json

from .external_request import get_pharmacy_request
from config import Config
from datetime import datetime
import pytz
import requests
from .lib import generate_pharmacies_attachement, filter_pharmacies_by_date, generate_menu_attachement


format_date = '%d/%m/%y'
madagascar_tz = pytz.timezone("Africa/Nairobi")
date_in_madagascar = datetime.now(madagascar_tz)
current_date = date_in_madagascar.strftime(format_date)


class GenericMessage:
    default_message = "Que puis je faire pour vous ?"
    sorry_message = "Il semble que nous n'ayons pas l'information que vous recherchez actuellement sur cette région."

def check_pharmacie(code, sender_id, bot):
    print(code)
    all_pharmacy = get_pharmacy_request(code)
    if all_pharmacy =='':
        bot.send_text_message(sender_id, GenericMessage.sorry_message)
        return
    filtered_pharmacies = filter_pharmacies_by_date(all_pharmacy, current_date, format_date)
    generate_pharmacies_attachement(sender_id, filtered_pharmacies, bot)


def handle_postback_event(event,bot):
    sender_id = event['sender']['id']
    postback = event['postback']
    if postback['payload'] == 'pharmacie':
        generate_menu_attachement(sender_id,bot)
    # Check if first time interaction
    if "first_time" in postback.get("payload"):
        send_welcome_message(sender_id)

def handle_message_event(event):
    sender_id = event['sender']['id']
    message = event['message']

    if "quick_reply" in message and "first_time" in message["quick_reply"].get("payload"):
        send_welcome_message(sender_id)

def send_welcome_message(sender_id):
    message = {
        "recipient": {
            "id": sender_id
        },
        "message": {
            "text": "Bienvenue sur notre bot Pharmacie de garde !"
        }
    }
    send_api_message(message)

def send_api_message(message,):
    url = f"https://graph.facebook.com/v15.0/me/messages?access_token={Config.ACCESS_TOKEN}"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(message))
    print(response.json())


