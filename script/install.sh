#!/usr/bin/env bash

if ! command -v /usr/sbin/tsn &> /dev/null
# If TSN executable doesn't exist
then
    ln -s ${TSN_HOME}/tsn.sh /usr/sbin/tsn
    echo "Created '/usr/sbin/tsn'"
fi

if [[ ! -f /etc/tsn.conf ]]
# If TSN configuration doesn't exist
then
    ln -s ${TSN_HOME}/config/settings.json /etc/tsn.conf
    echo "Created '/etc/tsn.conf'"
fi

echo "TSN installation finished"