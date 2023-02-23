#!/usr/bin/env bash

if [[ $EUID != "0" ]]
then
    echo "You must run this command as sudo"
    exit 1
fi

function enable {
    # Shutdown Daemon
    echo "TSN daemon (enable)"
    ln -s /opt/tsn/services/tsnd.service /lib/systemd/system/tsnd.service
    systemctl enable tsnd
    systemctl daemon-reload
    systemctl start tsnd
}

function disable {
    # Shutdown Daemon
    echo "TSN daemon (disable)"
    systemctl daemon-reload
    systemctl stop tsnd
    systemctl disable tsnd
    unlink /lib/systemd/system/tsnd.service
}

if [[ $1 == 'enable' ]]
then
    enable
elif [[ $1 == 'disable' ]]
then
    disable
else
    echo "Incorrect arguments (enable/disable)"
fi