#!/usr/bin/env python3
from telethon import TelegramClient
from telethon import events, sync
from telethon import functions, types
# Use your own values from my.telegram.org
api_id = 5182767
api_hash = '559d7a72eee8756e2df3e4db9eeac632'

client = TelegramClient('xxx', api_id, api_hash).start()
saved_path = ''

CHANNEL1 = 'https://t.me/ethio_0nline'
CHANNEL2 = 'https://t.me/qnashcom'
MY_CHANNEL = 'https://t.me/lalimartet'
MY_CHANNEL2 = 'https://t.me/joinchat/c0zw5lfNTak2MzA9'


@client.on(events.NewMessage(MY_CHANNEL))
async def my_event_handler(event): 
    if event.photo: 
        saved_path = await event.download_media('./img')
        await client.send_message(MY_CHANNEL, event.text, file=saved_path)
        print(saved_path)
@client.on(events.NewMessage(MY_CHANNEL2))
async def my_event_handler(event): 
    if event.photo: 
        saved_path = await event.download_media('./img')
        await client.send_message(MY_CHANNEL, event.text, file=saved_path)
        print(saved_path)
    


def process_message(event): 
    pass    

client.run_until_disconnected()