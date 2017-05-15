# Requirements
beautifulsoup (`aptitude install python3-bs4`)

make sure that the fr_FR.utf8 locales are installed

# doctolib

This script checks every x seconds (between 10 and 60 seconds) whether an appointement for a doctor is free before a set date.

If a date has been freed, it will send a mail to tell the user.

Currently works with the university of lille 3 mails but can be easily changed to work with any smtps compatible mail server.

Usage :
```
usage: doctolib.py [-h] -t TO -f SENDER -d DATE -u URL

optional arguments:
  -h, --help            show this help message and exit
  -t TO, --to TO        set the mail of the receiver
  -f SENDER, --from SENDER
                        set the mail of the sender
  -d DATE, --date DATE  format : dd-mm-yyyy. Sets the date before which we
                        send a mail
  -u URL, --url URL     set the url to check
```

# To run in the background
To suspend : `Ctrl Z`

To start in background : `bg %[job]`

To remove from the terminal : `disown %[job]`

# How to get the URL
Go on the URL of the doctor you want an appointement with

Right click on the page and go to Network

Reload

Change the week for the appointement

On the network window, click on the last GET and look at the address on the right panel ("Request URL").

Use this URL as the -u argument (you can change the date if needed).


