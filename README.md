Script to alert whenever there are Images posted to a Telegram group
This script can be used to moniter a telegram group to track dropbox slot availability

There are two alerts whenever an:
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
win10toast



Just start the script from the terminal or use a batch/Cron job to run the script. When the script is started, it will request authentication

Works on Windows 10. In order to make it work for other platforms, remove the dependency from win10toast in the script and it should work

Code authored by Arun Jaganathan 