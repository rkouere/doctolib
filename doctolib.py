# needs beautifulsoup (aptitude install python3-bs4)
# make sure that the fr_FR.utf8 locales are installed

import urllib.request
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime
import locale
import argparse
import sys
from random import randint
import time
from getpass import getpass
import json
import os

# we make sure that we use the french locale
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')

receivers = []

message = """From: From You You You <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: doclib is free. Hurry up !

"""

log_file = "log.txt"

def my_print(text):
    if os.path.exists(log_file):
        with open(log_file, "a") as f:
            f.write(text + "\n")

    else:
        with open("log.txt", "w") as f:
            f.write(text + "\n")

def send_mail(sender, receivers, message, psswd):
    '''
    Sends a mail
    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, psswd)
    server.sendmail(sender, receivers, message)
    server.quit()
    my_print("Successfully sent email")


def get_page(url):
    '''
    Get the html of the url
    '''
    page_html = urllib.request.urlopen(url)
    return page_html


def get_next_appointement(content):
    '''
    Get the next date available
    '''
    soup = BeautifulSoup(content, "lxml")
    dates = soup.findAll("p")
    jsonDate = json.loads(str(dates[0])[3:-4])
    return datetime.strptime(jsonDate["next_slot"], '%Y-%m-%d')

#send_mail(sender, receivers, message)


def main():
    # Install the argument parser. Initiate the description with the docstring
    argparser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__)
    # this is a option which need one extra argument
    argparser.add_argument("-t",
                           '--to',
                           required=True,
                           help="set the mail of the receiver")
    argparser.add_argument("-f",
                           '--from',
                           required=True,
                           dest="sender",
                           help="set the mail of the sender")
    argparser.add_argument('-d',
                           "--date",
                           required=True,
                           help="""format : dd-mm-yyyy. Sets the date before
                            which we send a mail""")
    argparser.add_argument('-u',
                           "--url",
                           required=True,
                           help="set the url to check")

    arguments = argparser.parse_args()

    # sets the arguments
    receivers.append(arguments.to)
    sender = arguments.sender
    url = arguments.url
    content = get_page(url)
    next_appointement = get_next_appointement(content)
    appointement_wanted = datetime.strptime(arguments.date, '%d-%m-%Y')

    auth_pwd = getpass('SMTP password for the sender')

    while True:
        if(appointement_wanted > next_appointement):
            send_mail(sender, receivers, message, auth_pwd)
            with open(log_file, "a") as f:
                f.write("appointement wanted = {}\n".format(appointement_wanted))
                f.write("next appointement = {}\n".format(next_appointement))
      
            sys.exit()
        else:
            content = get_page(url)
            next_appointement = get_next_appointement(content)
            with open("log.txt", "w") as f:
                f.write("{}: {}\n".format(time.strftime("%H:%M:%S"), next_appointement))
            time.sleep(randint(10, 60))

# This is a Python's special:
# The only way to tell wether we are running the program as a binary,
# or if it was imported as a module is to check the content of
# __name__.
# If it is `__main__`, then we are running the program
# standalone, and we run the main() function.
if __name__ == "__main__":
    main()
