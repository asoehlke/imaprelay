import imaplib
import smtplib
import logging

log = logging.getLogger(__name__)

def make_imap_connection(config):
    # Connect to the server
    hostname = config['hostname']
    log.info('Connecting to IMAP server {0}'.format(hostname))
    connection = imaplib.IMAP4_SSL(hostname)

    # Login to our account
    username = config['username']
    password = config['password']
    log.info('Logging in to IMAP as {0}'.format(username))
    connection.login(username, password)

    return connection

def make_smtp_connection(config):
    # Connect to the server
    hostname = config['hostname']
    log.info('Connecting to SMTP server {0}'.format(hostname))
    connection = smtplib.SMTP_SSL(hostname)

    # Login to our account
    username = config['username']
    password = config['password']
    log.info('Logging in to SMTP as {0}'.format(username))
    connection.login(username, password)

    return connection
