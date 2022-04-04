#!/usr/bin/env bash
# This script should have a symbolic link to /etc/profile.d

# On SSH connection
if [[ ! -z ${SSH_CONNECTION} ]]; then
    # Run the python script
    stringarray=($SSH_CONNECTION);
    /usr/sbin/tsn session ${stringarray[0]};
fi