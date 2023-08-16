from flask import request, Blueprint
from pymessenger.bot import Bot
from config import Config
from lib.access_page import access_page
from .lib import generate_menu_attachement, quick_response
from .message import check_pharmacie, GenericMessage, handle_message_event, handle_postback_event

pharmacy_guard = Blueprint("pharmacie", __name__, url_prefix=f'{Config.CONTEXTE_PATH}')

@pharmacy_guard.route("/pharmacie", methods=['GET', 'POST'])
def receive_message():
    generic_bot = Bot(Config.ACCESS_TOKEN)
    if request.method == 'GET':
        """Verification token"""
        return access_page(Config.VERIFY_TOKEN)

    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                recipient_id = message['sender']['id']
                if message.get('message'):
                    handle_message_event(message)
                    generic_bot.send_text_message(recipient_id, GenericMessage.default_message)
                    generate_menu_attachement(recipient_id, generic_bot)
                    quick_response(recipient_id, generic_bot)

                elif message.get('postback'):
                    handle_postback_event(message,generic_bot)
                    payload = message['postback']['payload']
                    check_pharmacie(payload,recipient_id,generic_bot)
                    quick_response(recipient_id, generic_bot)

    return "Message Processed"
