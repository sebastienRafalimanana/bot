# envoie message vers l'utilisateur
def send_message(recipient_id, response, bot_agent):
    # send message to user
    bot_agent.send_text_message(recipient_id, response)
    return "success"
