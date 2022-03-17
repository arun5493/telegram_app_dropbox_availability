# About:
A basic CLI app that can be used to <i><b> efficiently monitor </b></i> a telegram group that tracks H1B Dropbox/Regular slot availability  

An alert is sounded whenever an image is posted in a telegram group.  
Want to check the latest "NA" message from the group? Just look at the output of the script

There are two alerts whenever an image is posted or if the incoming message has the keyword "available":
1. A beep sound
2. Windows 10 toast notification (with a duration of 20 seconds)

# Prerequisites:

1. Telegram account
2. Be a member of the group based on your requirement- H1B/H4 Visa Dropbox slots( No Questions only slot availability messages) OR H1B/H4 Regular visa slots( No Questions only slot availability messages)

# Requirements:  

- Python3
- Pip
- Telethon
- beepy
- win10toast (for windows only)

Note: Telethon, beepy and wind10toast are python packages, so you can simply do a pip install

# Instructions:
Clone the repo. From the terminal, navigate to the place where the repo is cloned and run the following commands:

~~~~
> pip install telethon beepy
> pip install win10toast (For windows only)
> python *.py
~~~~

Just start the script from the terminal or use a batch/cron job to run the script. When the script is started, it will request authentication

Download the script based on your platform.

Code authored by <b>Arun Jaganathan</b>
