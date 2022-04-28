#!/usr/bin/env python3

# Script to detect changes on public ip's
# Should be called from a 'cron' job

import re
import os
import tools

config = tools.get_config()
IP_FILE = config["API"]["public_ip"]["file"]


def save_ip_file(filename: str, ip: str):
    file = open(filename, 'w')
    file.write(ip)
    file.close()


def create_ip_file(filename: str):
    file = open(filename, 'x')
    file.close()
    save_ip_file(filename, tools.get_publicip())


def load_ip_file(filename: str):
    file = open(filename, "r")
    ip = file.read()
    file.close()

    if bool(re.match(r'([0-9]+\.){3}[0-9]+', ip)):
        return ip

    else:
        return None


# Main Code

try:
    # Load the IP
    ip_addr = load_ip_file(IP_FILE)
    new_ip = tools.get_publicip()

    # If IP not valid, recreate ID (rare)
    if ip_addr == None:
        save_ip_file(IP_FILE, new_ip)

    # If new ip is different
    if ip_addr != new_ip:
        save_ip_file(IP_FILE, new_ip)
        os.system(f'{tools.TSN_BIN} notify ip_new now')

except:
    create_ip_file(IP_FILE)
