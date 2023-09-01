#!/bin/sh

# If PAM_TYPE is login
if [ "$PAM_TYPE" = "open_session" ]; then
	exec /usr/sbin/tsn session $SSH_CONNECTION
fi
