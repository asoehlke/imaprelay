imaprelay
=========

``imaprelay`` is a simple tool designed to scratch a very specific itch.
Presented with an institutional email account that he had an obligation
to check, but lacking desire to use the Outlook Web Access interface, the
author was dismayed to find that he was unable to forward his email.

The solution is ``imaprelay``, a python program that logs into an IMAP
account and relays emails from the Inbox to a specified email address,
via an SMTP server. Once relayed, emails are "archived" -- moved out of
the inbox into a different folder.

Although usable programmatically [#code]_, it is expected that most people
will  want to use the ``imaprelay`` command-line tool that this package
provides.

By default, this program will look for a configuration file in
``~/.secret/imaprelay.cfg`` -- its location should indicate that it needs
to contain plain-text passwords for IMAP and SMTP servers, and thus the
program will exit immediately if the file is group- or world-readable.

The available configuration options are listed below::

    # IMAP server connection details
    [imap]
    hostname=imap.exchange.megacorp.com
    username=j.bloggs
    password=123password
    
    # SMTP server connection details
    [smtp]
    hostname=mail.recipient.com
    username=joe_bloggs
    password=passw0rd
    
    # Relay configuration
    [relay]
    # Who should we relay the emails to?
    to=onward@recipient.com
    # Where should we look for emails to be relayed?
    inbox=INBOX
    # Where should we move the emails once successfully relayed?
    archive=Archive

Once you've written a config file, all you need to do is run::

    imaprelay

For verbose logging, use::

    imaprelay -v

Bug reporting
*************

Please report bugs `on Github <http://github.com/nickstenning/imaprelay/issues>`_.


.. [#code] See the ``imaprelay.Relay`` class.

136  python3 command.py
  137  cd imaprelay/
  138  python3 command.py
  139  cd docker
  140  ls
  141  cd ha_alpine386/
  142  docker build -tag alpine386 .
  143  docker build --tag alpine386 .
  144  docker build --build-arg BUILD_VERSION=v3.12 --tag alpine386v3.12 .
  145  docker build --build-arg BUILD_VERSION=v3.12.0 --tag alpine386v3.12 .
  146  docker build --build-arg BUILD_VERSION=v3.11.0 --tag alpine386v3.12 .
  147  docker build --build-arg BUILD_VERSION=3.12 --tag alpine386v3.12 .
  148  cd ..
  149  cd imaprelay/
  150  docker build --build-arg BUILD_FROM=~/docker/ha_alpine386  .
  151  ls ~/docker/ha_alpine386
  152  docker ls
  153  docker ps
  154  docker images
  155  docker build --build-arg BUILD_FROM=7336b031730a  .
  156  docker images
  157  docker build --build-arg BUILD_FROM=7336b031730a --tag imaprelay0.1 .
  158  docker images
  159  docker run 8ba3def14ac7
  160  docker build --build-arg BUILD_FROM=7336b031730a --tag imaprelay0.1 .
  161  docker run 8ba3def14ac7
  162  ls
  163  docker build --build-arg BUILD_FROM=7336b031730a --tag imaprelay0.1 .
  164  docker run 8ba3def14ac7
  165  docker build --build-arg BUILD_FROM=7336b031730a --tag imaprelay0.1 .
  166  docker images
  167  docker run c142c0c19180
  168  docker build --build-arg BUILD_FROM=7336b031730a --tag imaprelay0.1 .
  169  docker run imaprelay0.1:latest
  170  cd ..
  171  tar -czvf imaprelay.tgz imaprelay
  172  cd .ssh
  173  ls
  174  cat id_rsa.pub
  175  cd
  176  ssh 192.168.178.15
  177  ssh 192.168.178.15:22
  178  ssh 192.168.178.15 -p 22
  179  ssh 192.168.178.15 -p 22 -i ~/.ssh/id_rsa 
  180  ssh root@192.168.178.15 -p 22 -i ~/.ssh/id_rsa 
  181  scp imaprelay.tgz root@192.168.178.15:/addons
  182  ssh root@192.168.178.15 -p 22 -i ~/.ssh/id_rsa 
  183  tar -czvf imaprelay.tgz imaprelay
  184  scp imaprelay.tgz root@192.168.178.15:/addons
  185  ssh root@192.168.178.15 -p 22 -i ~/.ssh/id_rsa 
  186  tar -czvf imaprelay.tgz imaprelay
  187  scp imaprelay.tgz root@192.168.178.15:/addons
  188  ssh root@192.168.178.15 -p 22 -i ~/.ssh/id_rsa 
  189  cd imaprelay/
  190  vi run.sh 
  191  cd ..
  192  tar -czvf imaprelay.tgz imaprelay
  193  scp imaprelay.tgz root@192.168.178.15:/addons
  194  ssh root@192.168.178.15 -p 22 -i ~/.ssh/id_rsa 
  195  tar -czvf imaprelay.tgz imaprelay
  196  scp imaprelay.tgz root@192.168.178.15:/addons
  197  ssh root@192.168.178.15 -p 22 -i ~/.ssh/id_rsa 
  198  ls -ltr
  199  cd /mnt
  200  ls
  201  cd c
  202  ls
  203  cd tmp
  204  cp ~/imaprelay.tgz .
  205  history
