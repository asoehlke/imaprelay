imaprelay
=========

This program will look for a configuration file in ~/.secret/imaprelay.json -- its location 
should indicate that it needs to contain plain-text passwords for IMAP and SMTP servers, 
and thus the program will exit immediately if the file is group- or world-readable.

The available configuration options are listed below::
{
    "imap": {
        "hostname": "imap.myserver.de",
        "username": "...",
        "password": "..."
    },
    "smtp": {
        "hostname": "smtp.myserver.de",
        "username": "...",
        "password": "..."
    },
    "relay": {
        "interval": 10,
        "inbox": "INBOX",
        "archive": "Archive",
        "error": "Error",
        "from": "forwarder@myserver.de",
        "sender": "catchall@myserver.de",
        "recipients" : [
            {
                "name": "Andreas",
                "filter": "TO andreas",
                "to": "andreas@myserver.de"
            },
            {
                "name": "all",
                "filter": "ALL",
                "to": "andreas@myserver.de"
            }
        ]
    }
}

Once you've written a config file, all you need to do is run::

    imaprelay

For verbose logging, use::

    imaprelay -v
