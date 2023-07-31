import random
from flask import Blueprint,request
from pymessenger.bot import Bot

education = Blueprint("education",__name__)
ACCESS_TOKEN = 'EAAECHxkNCc0BOzmWOGwj7xMmBITos0AMMOXlxRe4pVl2VNY3FzjvwvnYXVZCeefJiFOg95P3uhjYgu6ZAvZCx74VpsWVNbk8fjVmaHUsL7SBZCJsefjefpZB6P161fHazkmghQGe5ojJZArnKJL9RmauK80I5GyBwBwQNP6QHFVMAF4vCcXoZCaX7Ktp9H3LXii'
VERIFY_TOKEN = '2kl73mjy1e'
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint
@education.route("/education", methods=['GET', 'POST'])

def receive_message():
    if request.method == 'GET':
      return "I'am education bot"


