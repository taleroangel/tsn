#!/usr/bin/env python3

# Script that manages sending notifications to Telegram
# Checks within configuration file if enabled
# Also contains all messages

# AVAILABLE COMMANDS
# -- config.json
# startup
# shutdown
# newip
# ssh_newcon [ip]
# -- shell onlu
# getip
# message [message]
# alert [message]

# Libraries
import sys
import tools
import telegram

# Main code
conf = tools.get_config()


def notification_newconnection(protocol: str, ipaddr: str):
    return f'🔌 ({protocol.upper()}) Detected new connection\nFrom IP: *{ipaddr}*'


# defined inside config.json
try:
    # Startup
    if (sys.argv[1] == 'startup') and conf["settings"]["general"]["startup"]:
        telegram.send(f'🟢 Server is active!\nListening for connections...')
        telegram.send(
            f'🌎 Server\'s public address is: *{tools.get_publicip()}*')

        # Shutdown
    elif (sys.argv[1] == 'shutdown') and conf["settings"]["general"]["shutdown"][0]:
        telegram.send(
            f'🔴 Server is shutting down!\nConnections will be closed soon...')

        # IP change
    elif (sys.argv[1] == 'newip') and conf["settings"]["general"]["newip"][0]:
        telegram.send(
            f'⚡ Server\'s IP address has changed!\nNew IP address is: *{tools.get_publicip()}*')

        # SSH connection
    elif (sys.argv[1] == 'ssh_newcon') and conf["settings"]["ssh"]["newcon"]:
        telegram.send(notification_newconnection('ssh', sys.argv[2]))

    # shell available commands
        # Show IP
    elif sys.argv[1] == 'getip':
        telegram.send(
            f'🌎 Server\'s public address is: *{tools.get_publicip()}*')

        # Show message
    elif sys.argv[1] == 'message':
        telegram.send(f'🖥️ Server\'s message: {sys.argv[2]}')

		# Show alert
    elif sys.argv[1] == 'alert':
        telegram.send(f'⚠️ ALERT: {sys.argv[2]}')

except:
    tools.print_err("Invalid 'notification module' usage")
