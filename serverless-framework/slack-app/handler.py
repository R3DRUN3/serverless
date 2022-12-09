import os
import sys
import json
from datetime import datetime as dt
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./vendored"))


SLACK_TOKEN = os.environ['SLACK_TOKEN']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']


def hello(event, context):
    try:
        print('Received message, writing it to slack channel!')
        data = event['data']
        message = json.loads(data)
        write_to_slack = f"{message} - written at {date_time}"
        date_time =  dt.now().strftime("%d/%m/%Y, %H:%M:%S")
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel="#"+SLACK_CHANNEL, text=write_to_slack)
        print('Procedure OK')
    except Exception as e:
        print(f"ERROR: {e}")
        return {"statusCode": 500}
    return {"statusCode": 200}