# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *


def gui():
    root = Tk()
    root.title("Windows KeyLogger")
    root.geometry("300x200")

    login_label = Label(text="LogIn").grid(row=0, column=0, columnspan=2, sticky=W)
    email_label = Label(text="Email").grid(row=2, column=0, columnspan=1, sticky=W)

    usr_email = StringVar()

    email = Entry(width=20, textvariable=usr_email)
    email.grid(row=5, column=0, columnspan=4, sticky=W)

    usr_pswd = StringVar()
    pswd_label = Label(text="Password").grid(row=6, column=0, columnspan=1, sticky=W)

    pswd_entry = Entry(width=20, show="*")
    pswd_entry.grid(row=7, column=0, columnspan=4, sticky=W)

    submit = Button(text="Submit")
    submit.grid(row=9, column=1)

    
    def save3_var():
        """Save the users entry as a variable inorder to be used in 
           users email and pasword function 
        """
        global var1, var2

        var1 = str(usr_email.get())
        var2 = str(usr_pswd.get())

    save3_var()

    root.mainloop()

# creating a gui interface in a dunction to make it callable in the keylogger script





