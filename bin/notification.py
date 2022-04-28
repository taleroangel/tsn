#!/usr/bin/env python3

""" Script that manages sending notifications to Telegram
Checks within configuration file if enabled
Also contains all messages

# AVAILABLE COMMANDS
# -- config.json
- startup now
- shutdown now
- ip_new now
- ssh [ip]
# Shell commands
- ip_show now
- message [message]
- alert [message]

"""

# Libraries
import sys
import tools
import telegram
import cmd

# Get the configuration files
conf = tools.get_config()


def connection(protocol: str, ipaddr: str) -> str:
    return f'🔌 ({protocol.upper()}) Detected new connection\nFrom IP: *{ipaddr}*'


def message(message: str) -> str:
    return f'🖥️ *Server message:* {message}'


def alert(message: str) -> str:
    return f'⚠️ *ALERT:* {message}'


try:
    # !! List of available commands
    commands = [
        # * General
        # Statup command
        cmd.Command('startup', [
            lambda x: telegram.send_message(
                f'🟢 Server is active!\nListening for connections...'),
        ], conf["settings"]["general"]["startup"]),

        # Shutdown command
        cmd.Command('shutdown', [
            lambda x: telegram.send_message(
                f'🔴 Server is shutting down!\nConnections will be closed soon...')
        ], conf["settings"]["general"]["shutdown"]),

        # IP change
        cmd.Command('ip_new', [
            lambda x: telegram.send_message(
                f'⚡ Server\'s IP address has changed!\nNew IP address is: *{tools.get_publicip()}*')
        ], conf["settings"]["general"]["newip"]),

        # Send a message
        cmd.Command('message', [
            lambda x: telegram.send_message(message(" ".join(x)))
        ]),

        # Send an alert
        cmd.Command('alert', [
            lambda x: telegram.send_message(alert(" ".join(x)))
        ]),

        # Get IP
        cmd.Command('ip_show', [
            lambda x: telegram.send_message(
                f'🌎 Server\'s public address is: *{tools.get_publicip()}*')
        ]),

        # * Protocols

        # SSH connection
        cmd.Command('ssh', [
            lambda x: telegram.send_message(connection('ssh', sys.argv[2]))
        ], conf["services"]["ssh"])
    ]

    #! END

    # Parse commands
    cmd.interpret_command(sys.argv[1], commands, sys.argv[2:])

except Exception:
    tools.print_err("Incorrect usage of 'notification.py'")
