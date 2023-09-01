#!/usr/bin/python3
# Script that manages sending notifications to Telegram

# Libraries
import tools
import sys

try:
    conf = tools.load_settings()['notifications']

    # Get arguments
    COMMAND = sys.argv[1]
    ARGS = sys.argv[2:]

    # Parse message
    message = conf[COMMAND]

    try:
        i = 0
        while message.find("{}") > 0:
            message = message.replace("{}", ARGS[i], 1)
            i = i + 1

        # Send message
        tools.telegram_send(message)

    except:
        tools.print_error("Invalid arguments")

except:
    tools.print_error("Unable to load message")
