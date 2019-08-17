# Keylogger_with_GUI
Wanted to create a keylogger with a more friendly U.I with GUI.
Hello !

Am working on designing a GUI keylogger that will be User Friendly even to someone who has zero knowledge of python.

The Keylogger is designed to send the keyboard inputs(logs) to the email which the user will provide after a certain span of time or after every 100 characters.

Sample of the GUI :

Nb: 

The options will be between time (between 30minutes to 24 hours) and number  of characters (between 200 -2000 characters).

If you need to check if the code works. There is a .exe file you can run then you can input 100 character while connected to the internet to see if you will receive the  .txt attachment file of the logs.

…..to setup g mail in order for it to work you need to follow the procedure that will be provided by  google..

Go to the Keylogger_with_GUI/dist/KEYlogger.exe

OR 

Keylogger_with_GUI/build/KEYlogger/KEYlogger.exe

or Keylogger_with_GUI/dist/KEYlogger/KEYlogger.exe

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

If new to Python here is a little walkthrough of what has been coded , the tools used and the modules for the program to run succesfully.

The key logger is designed to send the logs after every 100 characters. But the network connection is not available it stores the logs in a temporary file, that is , if the script is still running.

To  run the script with no trouble you will need to have a python environment and most likely on a Windows based OS. You can download the Python IDE from https://www.python.org or maybe download Pycharm 2019 (Community Edition: its free) from https://www.jetbrains.com .

Then Follow The steps:

Using pycharm

After instillation, open Pycharm IDE ,Go to new project and create a new project with a virtual environment.

After creating , you will need to configure the interpreter .

Go to Settings>Project:Name_you_used>project add interpreter(add the default interpreter) press ok.

After you configure the interpreter , There is a + button ,click on it to add the packages needed .

On the search box type winshell then install package. Do the same for the other packages

pynput

pywin32

After installation exit that window, click apply then ok then restart Pycharm.

Please make sure you have installed python from https://www.python.org. You can also put the packages where they are needed mannually when you run the script it will indicate the error of the missing file showing where they are supposed to be and you can copy paste them-they are attached in the zip file .

Thank you and feel free to add or remove anything only if it is necessary.

 
