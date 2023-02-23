#!/usr/bin/env python3

# Script to detect changes on public ip's
# Should be called from a 'cron' job

import re
import os
import sys
import tools

config = tools.load_settings()
IP_FILE = config["api"]["ip"]["file"]


def save_ip_file(filename: str, ip: str):
    file = open(filename, 'w')
    file.write(ip)
    file.close()


def create_ip_file(filename: str):
    file = open(filename, 'x')
    file.close()
    save_ip_file(filename, tools.public_ip())


def load_ip_file(filename: str):
    file = open(filename, "r")
    ip = file.read()
    file.close()

    if bool(re.match(r'([0-9]+\.){3}[0-9]+', ip)):
        return ip

    else:
        return None


try:
    # Load the IP
    ip_addr = load_ip_file(IP_FILE)
    new_ip = tools.public_ip()

    # If IP not valid, create the file with the new IP
    if ip_addr == None:
        save_ip_file(IP_FILE, new_ip)

    # If new ip is different
    elif ip_addr != new_ip:
        save_ip_file(IP_FILE, new_ip)
        os.system(f'{tools.TSN_BIN} notify new_ip {new_ip}')

    if len(sys.argv) > 1 and sys.argv[1] == 'show':
        os.system(f'{tools.TSN_BIN} notify public_ip {new_ip}')


except:
    create_ip_file(IP_FILE)
    os.system(f'{tools.TSN_BIN} notify new_ip {tools.public_ip()}')
    tools.print_error("IP file didn't exist, created.")
