from flask import request, Blueprint
from pymessenger.bot import Bot
from lib.access_page import access_page
from lib.send_message import send_message
from.flow import handle_weather_command



ACCESS_TOKEN = 'EAAECHxkNCc0BOzmWOGwj7xMmBITos0AMMOXlxRe4pVl2VNY3FzjvwvnYXVZCeefJiFOg95P3uhjYgu6ZAvZCx74VpsWVNbk8fjVmaHUsL7SBZCJsefjefpZB6P161fHazkmghQGe5ojJZArnKJL9RmauK80I5GyBwBwQNP6QHFVMAF4vCcXoZCaX7Ktp9H3LXii'
VERIFY_TOKEN = '2kl73mjy1e'
bot_demo = Bot(ACCESS_TOKEN)

wealther = Blueprint("wealther", __name__)

#We will receive messages that Facebook sends our bot at this endpoint
@wealther.route("/wealther", methods=['GET', 'POST'])
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

