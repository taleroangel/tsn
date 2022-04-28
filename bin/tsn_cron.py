#!/usr/bin/env python3

"""Alter the system's crontab
"""

import re
import tools

CRONFILE = '/etc/crontab'


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
        tools.print_err("Crontab is not in compatible state")
        file_out = open(filename, 'a')
        file_out.write(
            f'\n# TSN_CRON (DO NOT MODIFY THIS COMMENT) #\n\n# TSN_CRON (DO NOT MODIFY THIS COMMENT) #\n')
        file_out.close()
        print("Crontab altered for enabling compatibility")


# Main code
# Fetch settings
config = tools.get_config()

# Store rules in this string
cron_rules: str = "\n"

# Check if crontab is TSN compatible
check_tsn_compatible(CRONFILE)

# Read SHUTDOWN time schedule
if bool(re.match(r'[0-2][0-9]:[0-5][0-9]', config["settings"]["general"]["shutdown"][1])):
    time = config["settings"]["general"]["shutdown"][1]
    hour, min = time.split(":", 1)
    cron_rules += f'{min} {hour} * * * root /usr/sbin/shutdown -h now\n'

# Read NEW_IP schedule
if config["settings"]["general"]["newip"][0]:
    minutes = config["settings"]["general"]["newip"][1]
    cron_rules += f'*/{minutes} * * * * root /usr/sbin/tsn updateip\n'

# Alter crontab
alter_crontab(CRONFILE, cron_rules)
print(f"Crontab rules updated:\n{cron_rules}")
