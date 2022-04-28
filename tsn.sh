#!/usr/bin/env bash

# Symbolik link from /sbin should be created

# Check if the script is runned by SUDO
function check_root {
    if [[ $EUID != "0" ]]
    then
        echo "You must run this command as sudo"
        exit 1
    fi
}

# Notify on login (Root is not required here)
if [[ $1 == "session" ]]; then
    exec /opt/tsn/bin/notification.py ${@:2}
elif [[ $1 == 'about' ]]
then
    echo "TSN (Telegram Server Notifications)"
    echo "Angel D. Talero (@taleroangel) © 2022"
	echo "Note: sudo access is required to use TSN shell"
	exit
fi

# Check for root privileges
check_root

# Manage notifications
if [[ $1 == "startup" ]]
then
	/opt/tsn/bin/notification.py startup now
	exec /opt/tsn/bin/notification.py ip_show now
elif [[ $1 == "shutdown" ]]
then
    exec /opt/tsn/bin/notification.py shutdown now
    
    # Send notification
elif [[ $1 == "notify" ]]
then
    exec /opt/tsn/bin/notification.py ${@:2};
    
# Update ip
elif [[ $1 == "updateip" ]]
then
    exec /opt/tsn/bin/ipcheck.py ${@:2};
    
elif [[ $1 == "service" ]]
then
    exec /opt/tsn/services/services.sh ${@:2};
    
    # Update cron
elif [[ $1 == 'update-conf' ]]
then
    # Update configuration
    echo "Updating configuration..."
    /opt/tsn/bin/tsn_cron.py;
    echo "Restarting cron service"
    systemctl restart cron;
    echo "Update completed!"
    
else
    echo "Invalid argument (refer to documentation for help)"
fi