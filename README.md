# 📫 Telegram Server Notifications (TSN)

## What is TSN?
TSN is a python script that notifies you about your server status via Telegram using the Telegram API and Telegram bots, TSN is capable of notifying you about the server being turned on, shutted down or rebooted, new SSH connections being made, changes in public IP addreses, and more..., this is configurable via /etc/tsn.conf and 'tsn' command line tool

## ⚠️ Security concerns
This folder and all the scripts must be located out of reach of non-sudo users becasue some of this scripts will be runned by 'cron' at startup with root priviliges.

## 🔍 Dependencies
- python3
- cron
- network-manager
- systemd

## 🌎️ Installation
/etc/tsn.conf and /usr/sbin/tsn

## 🧑‍🔬 TSN shell
TSN provides a command-line tool for sending messages and updating configurations defined in ['config.json'](#🧰-json-configuration-file-configjson)

### Usage
> tsn <_command_> <_arguments_>
- 'tsn' command must be runned as root

### Notification Commands
> **tsn notify [command]**
> Sends a message to Telegram server, available messages are defined in *tsn.conf*

> **tsn startup**
> Alias for 'notify startup' followed by 'ip show', used by *tsnd*

> **tsn shutdown**
> Alias for 'notify shutdown', used by *tsnd*

> **tsn session \<address\>**
> non-root alias to *tsn notify session \<address\>*\
> Sends a 'new session' notification, this is the only notification command that doesn't require Root for execution.

> **tsn ip [optional: show]**
> Updates public ip (usually called by cron), sends a message when ip changes\
> When the [show] argument is used, ip address will be send using 'notify public_ip'

> **tsn update-conf**
> Updates *tsn.conf* with cron rules

### Advanced Commands
> **tsn service [enable/disable]**
> Enables or disables tsnd.service (Required for startup and shutdown messages)

> **tsn install**
> Create required symbolic links for TSN to work properly

> **tsn remove**
> Remove TSN symbolic links

### Other commands
> **tsn about**
> Show information about TSN

## 🧰 tsn.conf (Configuration file)
### 'api' Section
#### telegram
* *api_key*: Telegram bot API key
* *group_id*: Chat ID where the bot will message to
#### public_ip
* *api_url*: API URL for getting public IP. ("https://ident.me", by default)
* *file*: File in which previous IP will be stored ("/opt/tsn/config/latest.ip", by default)