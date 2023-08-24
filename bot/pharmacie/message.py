from .external_request import get_pharmacy_request
from datetime import datetime
import pytz
from .lib import generate_pharmacies_attachement, generate_pharmacy_choice, filter_pharmacies_by_date, generate_menu_attachement,getLocalization
import re

format_date = '%d/%m/%y'
madagascar_tz = pytz.timezone("Africa/Nairobi")
date_in_madagascar = datetime.now(madagascar_tz)
current_date = date_in_madagascar.strftime(format_date)
localisation = getLocalization()


class GenericMessage:
    greeting_message = "Pharmacie de garde à Madagascar, nous vous souhaitons la bienvenu"
    default_message = "Pharmacie de garde à Madagascar,que puis je faire pour vous ?"
    pharmacie_message = "Pharmacie de garde à Madagascar, choisissez la région qui vous convient."
    sorry_message = "Il semble que nous ne disposons actuellement l'information que vous recherchez sur cette région."


def handle_postback_event(event,bot):
    sender_id = event['sender']['id']
    payload = event['postback']['payload']
    data = payload.split(";")
    if payload == "start":
        print("start")
        bot.send_text_message(sender_id, GenericMessage.greeting_message)
        generate_menu_attachement(sender_id, bot)
        return

    if payload == "pharmacie":
        print('pharmacie')
        bot.send_text_message(sender_id, GenericMessage.pharmacie_message)
        generate_menu_attachement(sender_id, bot)
        return

    #if user select state
    if len(data) == 1:
        bot.send_text_message(sender_id, f"Pharmacie de garde {localisation[int(payload)]}")
        check_pharmacie(payload, sender_id, bot)
        return

    # if user select choice permanant or hebdo
    if data[0] == "choice":
        all_pharmacy = get_pharmacy_request(data[2])
        if data[1] == "permanant":
            _, permanent_pharmacy = filter_pharmacies_by_date(all_pharmacy, current_date, format_date,False,True)
            bot.send_text_message(sender_id, f"Vous s'avez selectionné {data[3]}")
            generate_pharmacies_attachement(sender_id, permanent_pharmacy, bot)
            return
        else:
            hebdo_pharmacy,_ = filter_pharmacies_by_date(all_pharmacy, current_date, format_date, True, False)
            bot.send_text_message(sender_id, f"Vous s'avez selectionné {data[3]}")
            generate_pharmacies_attachement(sender_id, hebdo_pharmacy, bot)
            return

    # consult detail of pharmacy
    if len(data) == 3:
        bot.send_text_message(sender_id, f"Pharmacie {data[0]} \n\nTélephone: {data[2]}\n\nAdresse: {data[1]}")
        return

def handle_message_event(event, bot):
    sender_id = event['sender']['id']
    payload = event['message']
    try:
        if payload['quick_reply']['payload'] == "pharmacie":
            print('pharmacie')
            bot.send_text_message(sender_id, GenericMessage.pharmacie_message)
            generate_menu_attachement(sender_id, bot)
    except:
        bot.send_text_message(sender_id, GenericMessage.default_message)
        generate_menu_attachement(sender_id, bot)
        return

def check_pharmacie(code, sender_id, bot):
    print(code)
    all_pharmacy = get_pharmacy_request(code)
    if all_pharmacy =='':
        bot.send_text_message(sender_id, GenericMessage.sorry_message)
        return
    filtered_pharmacies, permanent_pharmacy = filter_pharmacies_by_date(all_pharmacy, current_date, format_date)
    if not permanent_pharmacy:
        generate_pharmacies_attachement(sender_id, filtered_pharmacies, bot)
    else:
        print("24h pharmacies")
        generate_pharmacy_choice(sender_id, code, bot)

