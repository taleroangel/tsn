#!/usr/bin/env bash

TSN_VERSION=1.2.0
export TSN_HOME=/opt/tsn

# Symbolik link to /usr/sbin/tsn must be created

# Check sudo permissions
function check_root {
    if [[ $EUID != "0" ]]
    then
        echo "You must run this command as sudo"
        exit 1
    fi
}

# Notify on login (Root is not required here)
if [[ $1 == "session" ]]; then
    exec ${TSN_HOME}/bin/notification.py session ${@:2}
    
elif [[ $1 == 'about' ]]
# Show about
then
    echo -e "$(which tsn) v${TSN_VERSION}"
    echo "TSN (Telegram Server Notifications)"
    echo "Angel D. Talero (@taleroangel) © 2023"
    exec echo "Contribute on GitHub: https://github.com/taleroangel/tsn"
fi

# Check for root privileges
check_root

# Manage notifications
if [[ $1 == "notify" ]]
# Send notification
then
    exec ${TSN_HOME}/bin/notification.py ${@:2};
    
elif [[ $1 == "startup" ]]
then
    ${TSN_HOME}/bin/notification.py startup;
    exec ${TSN_HOME}/tsn.sh ip show;
    
elif [[ $1 == "shutdown" ]]
then
    exec ${TSN_HOME}/bin/notification.py shutdown;
    
elif [[ $1 == "ip" ]]
# Update ip
then
    exec ${TSN_HOME}/bin/ipcheck.py ${@:2};
    
elif [[ $1 == "service" ]]
# Enable or disable the TSN service
then
    exec ${TSN_HOME}/services/services.sh ${@:2};
    
elif [[ $1 == 'update-conf' ]]
# Update cron
then
    # Update configuration
    echo "Updating configuration..."
    ${TSN_HOME}/bin/cron.py;
    echo "Restarting cron service"
    systemctl restart cron;
    echo "Update completed!"
    
elif [[ $1 == "install" ]]
# Create TSN symbolic links
then
    chmod +x ${TSN_HOME}/script/*
    exec ${TSN_HOME}/script/install.sh
    
elif [[ $1 == "remove" ]]
# Remove TSN symbolic links
then
    exec ${TSN_HOME}/script/remove.sh
    
else
    echo "Invalid argument (refer to documentation for help)"
fi