# 📫 Telegram Server Notifications (TSN)

## What is TSN?
TSN is a linux application that notifies you about your server status via Telegram using the Telegram API and Telegram bots, TSN is capable of notifying you about the server being turned on, shutted down or rebooted, new SSH connections being made, changes in public IP addreses, and more..., this is configurable via /etc/tsn.conf (symbolic link to /opt/tsn/config/config.json) and 'tsm' command line tool (/usr/sbin/tsm -> /opt/tsm/tsm.sh)

## ⚠️ Security concerns
This folder and all the scripts MUST be located out of reach of non-sudo users becasue some of this scripts will be runned by 'cron' at startup will root priviliges, any alteration to this files could result in a security hazard.

## 🔍 Dependencies
- python3
- cron
- network-manager
- systemd

## 🧑‍🔬 TSN shell
TSN provides a command-line tool for sending messages and updating configurations defined in ['config.json'](#🧰-json-configuration-file-configjson)

### Usage
> tsn <_command_> <_arguments_>
- 'tsn' command must be runned as root
- Arguments might only be required for certain commands

### Available commands
> **tsn notify [command]**
> Sends a message to Telegram server
>> #### Commands that work according to config.json
>> * _startup_: Show startup message
>> * _shutdown_: Show shutdown message
>> * _newip_: Show newip message
>> * _ssh_newcon [ip]_: Show new SSH connection
>> #### shell only commands
>> * _getip_: Shows current ip address
>> * _message [message]_: Send a generic message
>> * _alert [message]_: Send an alert

> **tsn update-conf**
> Updates 'cron' rules

> **tsn updateip**
> Updates public ip, usually called by cron, sends a message on new ip

### Advanced/Other commands
> **tsn service [enable/disable]**
> Enables or disables tsnd.service (Required for startup and shutdown messages)

> **tsn session [ipaddress]**
> Sends a 'SSH connection message', used by /etc/profile.d when a new session is created (Doesn't require root), 'ipaddress' is the IP of the SSH client

> **tsn startup**
> _tsn notify startup_ alias

> **tsn shutdown**
> _tsn notify shutdown_ alias

## 🧰 JSON Configuration file (config.json)
### API Section
#### telegram
* *api_key*: Telegram bot API key
* *group_id*: Chat ID where the bot will message to
#### public_ip
* *api_url*: API URL for getting public IP. ("https://ident.me", by default)
* *file*: File in which previous IP will be stored ("/opt/tsn/config/latestip.ip", by default)

### Settings Section
#### General
* *startup*: Send notification on startup
* *shutdown*: [Send notification on shutdown, Scheduled shutdown time in 'hh:ss', write 'disable' for disabling it]
* *newip*: [Send notification when the public ip changes, time in minutes until next check]

#### SSH
* *new_con*: Send notification on new connection

## ✅ TODO
- [x] Create a CLI interface
- [x] Create a startup/stop daemon
- [ ] Create an installation script
- [ ] Implement SFTP support