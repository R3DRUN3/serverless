import os
import sys
import json
import random

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./vendored"))

import requests

love_messages = ["I love U 💕", 
                 "I need you like a heart needs a beat ♥", 
                 "You are my heaven❤️", 
                 "You are my life ❤️",
                 "Take my hand, take my whole life too. For I can’t help falling in love with you 😘",
                 "I love you for all that you are, all that you have been and all that you will be 💕"] 

TOKEN = os.environ['TELEGRAM_TOKEN']
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)


def hello(event, context):
    try:
        data = json.loads(event["body"])
        response = ""
        message = str(data["message"]["text"])
        if "sofi" in message:
            response = random.choice(love_messages)
        else: 
            response = "Try writing 'sofi'"
        chat_id = data["message"]["chat"]["id"]
        first_name = data["message"]["chat"]["first_name"]

        data = {"text": response.encode("utf8"), "chat_id": chat_id}
        url = BASE_URL + "/sendMessage"
        requests.post(url, data)

    except Exception as e:
        print(e)

    return {"statusCode": 200}