from telethon import TelegramClient, events, sync
import beepy
import pytz

# to print the time stamp in EST
est = pytz.timezone('US/Eastern')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

# Values from my.telegram.org
#     Refer to this document on how to create your own ID and HASH either from
#       a. https://docs.telethon.dev/en/latest/basic/signing-in.html (OR)
#       b. https://core.telegram.org/api/obtaining_api_id
api_id = 00000000
api_hash = 'YOUR HASH GOES HERE'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats='H1B/H4 Visa Dropbox slots( No Questions only slot availability messages)'))
async def my_event_handler(event):
    msg = event.raw_text
    date = event.date
    photo = event.photo

    if photo is not None or "available" in str.lower(msg):
        print("----------------------ALERT sent at ",date.astimezone(est).strftime(fmt),"----------------------")
        beepy.beep(sound=4)
    elif "na" in str.lower(msg):
        print(msg, " at ", date.astimezone(est).strftime(fmt))

client.start()
client.run_until_disconnected()