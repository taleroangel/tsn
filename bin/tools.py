import requests
import json
import urllib.request

TSN_BIN = '/usr/sbin/tsn'
TSN_CONF = '/etc/tsn.conf'


def print_error(message: str):
    print(f"<tsn TelegramServerNotifications> ERROR: {message}")


def load_settings():
    try:
        config_json = open(TSN_CONF)
        config_data = json.load(config_json)
        config_json.close()
        return config_data

    except:
        print_error("Couldn't read configuration files")
        return None


def public_ip() -> str:
    PUBLIC_IP_API = load_settings()["api"]["ip"]["url"]
    return urllib.request.urlopen(PUBLIC_IP_API).read().decode('utf8')


def telegram_send(message: str):
    try:
        api = load_settings()["api"]["telegram"]
        API_CALL = f'https://api.telegram.org/bot{api["api_key"]}/sendMessage?chat_id={api["group_id"]}&parse_mode=Markdown&text='
        requests.get(API_CALL + message).json()
    except:
        print_error("Error while loading configuration")
