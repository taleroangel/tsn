# Libraries

# General tools used in every scripts

import json
import urllib.request

TSN_BIN = '/usr/sbin/tsn'


def print_err(message: str):
    print(f"<TelegramServerNotifications> ERROR: {message}")


def get_config():
    # Load the JSON config
    try:
        config_json = open(f'/opt/tsn/config/config.json')
        config_data = json.load(config_json)
        config_json.close()
        return config_data

    except:
        print_err("Couldn't read configuration files")
        return None


def get_publicip() -> str:
    PUBLIC_IP_API = get_config()["API"]["public_ip"]["api_url"]
    return urllib.request.urlopen(PUBLIC_IP_API).read().decode('utf8')
