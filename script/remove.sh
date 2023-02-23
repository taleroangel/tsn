#!/usr/bin/env bash

if command -v /usr/sbin/tsn &> /dev/null
then
    unlink /usr/sbin/tsn
    echo "Removed '/usr/sbin/tsn'"
fi

if [[ -f /etc/tsn.conf ]]
then
    unlink /etc/tsn.conf
    echo "Remove '/etc/tsn.conf'"
fi

echo "TSN removal finished"