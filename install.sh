#!/usr/bin/env bash

# Check that script is being runned as sudo
function check_root {
    if [[ $EUID != "0" ]]
    then
        echo "You must run this command as sudo"
        exit 1
    fi
}

function check_deps {
	if ! command -v cron &> /dev/null
	then
    	echo "required dependency 'cron' could not be found"
    	exit
	fi
	if ! command -v python3 &> /dev/null
	then
    	echo "required dependency 'python3' could not be found"
    	exit
	fi
	if ! command -v systemd &> /dev/null
	then
    	echo "required dependency 'systemd' could not be found"
    	exit
	fi
	if ! command -v nm &> /dev/null
	then
    	echo "required dependency 'network-manager' could not be found"
    	exit
	fi
}

function install {
    # Create TSN directory in OPT
    mkdir /opt/tsn
    mkdir /etc/tsn
	# Create cron backup
	cp /etc/crontab /etc/crontab.bak
	echo "INFO> '/etc/crontab' backup created in '/etc/crontab.bak'"
    # Copy contents of TSN into OPT
    cp -r `pwd`/* /opt/tsn/
    # Create required symbolic liks
    ln -s /opt/tsn/script/tsn_profile.sh /etc/profile.d/tsn_profile.sh
    ln -s /opt/tsn/tsn.sh /usr/sbin/tsn
    ln -s /opt/tsn/config/config.json /etc/tsn/config.json
    # Enable service
    /usr/sbin/tsn service enable
    # Change permissions
    chown -R root:root /opt/tsn
    chmod -R 0700 /opt/tsn
    chmod 0755 /opt/tsn
    chmod -R 0755 /opt/tsn/script
    chmod 0755 /opt/tsn/tsn.sh
    chown -R root:root /etc/tsn
    chmod 0755 /etc/tsn/config.json
    # Make binaries available
    chmod -R 0755 /opt/tsn/bin
    #BUG:#!! CONFIGURATION FILES ARE EXPOSED !!#
    chmod -R 0755 /opt/tsn/config
    # Show message
    echo "TSN has been installed on your system, please modify '/etc/tsn/config.json' and then run 'sudo tsn update-conf'"
}

function remove {
	# Disable service
	/usr/sbin/tsn service disable
	echo "INFO> tsn daemon was disabled and removed from systemd"
	# Remove links
	unlink /etc/tsn/config.json
	unlink /usr/sbin/tsn
	unlink /etc/profile.d/tsn_profile.sh
	echo "INFO> tsn binaries removed from the system"
	# Restore crontab
	rm /etc/crontab
	mv /etc/crontab.bak /etc/crontab
	echo "INFO> '/etc/crontab' was restored from '/etc/crontab.bak'"
	rm -rf /opt/tsn
	rm -rf /etc/tsn
	echo "INFO> TSN directory removed"
	echo "TSN was removed from your system"
}

check_root
check_deps

# Ask for installation or removal
read -p "Are you installing or removing tsn? (I/R): " operation
if [[ $operation == [iI] ]]
then
	install
elif [[ $operation == [Rr] ]]
then
	remove
fi
