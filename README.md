# Keylogger_with_GUI

A WindowsOS KeyLogger

The Keylogger is designed to send the keyboard inputs(logs) to the email which the user will provide after a certain span of time or after every 100 characters.


### Note: 

The options will be between time (between 30minutes to 24 hours) and number  of characters (between 200 -2000 characters).

### Set up
Create virtual environment
#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Run
```bash
python key_logger.py
```
To start off, input 100 character while connected to the internet to see if you will receive the  .txt attachment file of the logs.


The key logger is designed to mail the logs after every 100 characters but the network connection is not available it stores the logs in a temporary file, that is , if the script is still running.

### ToDo
- Add GUI


 
