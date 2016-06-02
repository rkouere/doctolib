# doctolib


This script checks every x seconds (between 10 and 60 seconds) whether an appointement for a doctor is free before a set date.

If a date has been freed, it will send a mail to tell the user.

Currently works with the university of lille 3 mails but can be easily changed to work with any smtps compatible mail server.

Usage :
```
usage: doctolib.py [-h] -t TO -f SENDER -d DATE -u URL [-p PASSWD]

optional arguments:
  -h, --help            show this help message and exit
  -t TO, --to TO        set the mail of the receiver
  -f SENDER, --from SENDER
                        set the mail of the sender
  -d DATE, --date DATE  format : dd-mm-yyyy. Sets the date before which we
                        send a mail
  -u URL, --url URL     set the url to check
  -p PASSWD, --pass PASSWD
                        Specify the password for given username. If not given,
                        script will prompt from stdin


```

# needs
beautifulsoup (`aptitude install python3-bs4`)
make sure that the fr_FR.utf8 locales are installed
