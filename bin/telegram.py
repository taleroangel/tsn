"""Sends a message through Telegram API
Takes a message to send as an argument
Reads API KEY from 'config.json'"""

import requests
import tools


def send_message(message: str):
    api = tools.get_config()
    # API URL
    API_CALL = f'https://api.telegram.org/bot{api["API"]["telegram"]["api_key"]}/sendMessage?chat_id={api["API"]["telegram"]["group_id"]}&parse_mode=Markdown&text='
    requests.get(API_CALL + message).json()
