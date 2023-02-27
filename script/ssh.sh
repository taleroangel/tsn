#!/bin/bash

if [ $PAM_TYPE == "open_session" ]; then
	/usr/sbin/tsn session $SSH_CONNECTION
fi