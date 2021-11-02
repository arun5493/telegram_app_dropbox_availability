Script to alert whenever there are Images posted to a Telegram group
This script can be used to moniter a telegram group to track dropbox slot availability

An alert is sounded whenever an image is posted in the telegram group.   
Want to check the latest "NA" message from the group? Just look at the output of the script

There are two alerts whenever an image is posted or if the incoming message has the keyword "available":
1. A beep sound using beepify
2. Windows 10 toast notification

Pre-req:
1. Telegram account
2. Be a member of the group - H1B/H4 Visa Dropbox slots( No Questions only slot availability messages)

Requirements:
Python3
Pip
Telethon
beepy
win10toast (for windows only)

Telethon, beepy and wind10toast are python packages, so you can simply do a pip install

Instructions:
From the terminal, navigate to the place where the script is stored and run the following commands:
pip install telethon beepy
pip install win10toast (For windows only)
python dropbox*.py

Just start the script from the terminal or use a batch/cron job to run the script. When the script is started, it will request authentication

Download the script based on your platform.

Code authored by Arun Jaganathan 
