from flask import request, Blueprint
from pymessenger.bot import Bot
from lib.access_page import access_page
from lib.send_message import send_message
from.flow import handle_weather_command



ACCESS_TOKEN = 'EAAb1T6xvZCtoBOZCrZAOFwu7sIVgxXYieARVKOVpEM7osqZAuwy7ibrR9EdqYVvyNaBf6KSuKnbP5KL2n8wvBQlAanUSs0sYtyUvBqH4pDTHkMqvcQxV1grSZAOBwNlTQ0eNx06jpzXhRSDkLDPNaZBIl6l2h7QaBl5sUqtiPZC9VsmPVTpWbf4sd0FP9tSZCj2a'
VERIFY_TOKEN = '2kl73mjy1e'
bot_demo = Bot(ACCESS_TOKEN)

wealther = Blueprint("meteo", __name__)

#We will receive messages that Facebook sends our bot at this endpoint
@wealther.route("/meteo", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Verification token"""
        return access_page(VERIFY_TOKEN)

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
                  send_message(recipient_id, response_sent_text, bot_demo)
    return "Message Processed"

