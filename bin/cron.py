#!/usr/bin/env python3

import re
import tools

CRON_FILE = '/etc/crontab'


def alter_crontab(filename: str, inputstr: str):
    """Alter contents of the 'tsn_cron' section in crontab"""

    # Read contents
    file_in = open(filename, 'r')
    data = file_in.read()
    file_in.close()

    # Replace contents
    file_out = open(filename, 'wt')

    # Replace everything inside '# TSN_CRON (DO NOT MODIFY THIS COMMENT) #' comments
    file_out.write(re.sub(r"\n?# TSN_CRON \(DO NOT MODIFY THIS COMMENT\) #\n(.*?)\n# TSN_CRON \(DO NOT MODIFY THIS COMMENT\) #\n?",
                          f'\n# TSN_CRON (DO NOT MODIFY THIS COMMENT) #\n{inputstr}\n# TSN_CRON (DO NOT MODIFY THIS COMMENT) #\n', data, flags=re.DOTALL))
    file_out.close()


def check_tsn_compatible(filename: str):
    """Check if crontab file is 'tsn_cron' compatible, if not, makes it tsn compatible"""
    file_in = open(filename, 'r')
    data = file_in.read()
    file_in.close()

    # Check if the file has TSN comments, if not, add them
    if data.find('# TSN_CRON (DO NOT MODIFY THIS COMMENT) #') == -1:
        tools.print_error("Crontab is not in compatible state")
        file_out = open(filename, 'a')
        file_out.write(
            f'\n# TSN_CRON (DO NOT MODIFY THIS COMMENT) #\n\n# TSN_CRON (DO NOT MODIFY THIS COMMENT) #\n')
        file_out.close()
        print("Crontab altered for enabling compatibility")


# Main code
config = tools.load_settings()

# Store rules in this string
cron_rules: str = "\n"

# Check if cron contains settings
check_tsn_compatible(CRON_FILE)

# Read NEW_IP schedule
if config["settings"]["ip"] is not None:
    minutes = config["settings"]["ip"]
    cron_rules += f'*/{minutes} * * * * root /usr/sbin/tsn ip\n'

# Alter crontab
alter_crontab(CRON_FILE, cron_rules)
print(f"Crontab rules updated:\n{cron_rules}")
