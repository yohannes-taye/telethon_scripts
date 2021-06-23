#!/usr/bin/env python3
from telethon import TelegramClient
from telethon import events, sync
from telethon import functions, types
# Use your own values from my.telegram.org
api_id = 5182767
api_hash = '559d7a72eee8756e2df3e4db9eeac632'

client = TelegramClient('xxx', api_id, api_hash).start()
saved_path = ''

#Ethio_Online_Market
CHANNEL1 = 'https://t.me/ethio_0nline'
#qnash.com - ቅናሽ
CHANNEL2 = 'https://t.me/qnashcom'
#ዘመነ ማርኬት
CHANNEL3 = 'https://t.me/buysellmarket1'
#ሱቄን በእጄ MARKET
CHANNEL4 = 'https://t.me/sukenbeje'
#Maki gifts
CHANNEL5 = 'https://t.me/makigifts'

MY_CHANNEL = 'https://t.me/lalimartet'
MY_CHANNEL2 = 'https://t.me/joinchat/c0zw5lfNTak2MzA9'


@client.on(events.NewMessage(CHANNEL1))
async def my_event_handler(event): 
    if event.photo: 
        saved_path = await event.download_media('./img')
        await client.send_message(MY_CHANNEL, event.text, file=saved_path)
        print(saved_path)
@client.on(events.NewMessage(CHANNEL2))
async def my_event_handler(event): 
    if event.photo: 
        saved_path = await event.download_media('./img')
        await client.send_message(MY_CHANNEL, event.text, file=saved_path)
        print(saved_path)

@client.on(events.NewMessage(CHANNEL3))
async def my_event_handler(event): 
    if event.photo: 
        saved_path = await event.download_media('./img')
        await client.send_message(MY_CHANNEL, event.text, file=saved_path)
        print(saved_path)
        
@client.on(events.NewMessage(CHANNEL4))
async def my_event_handler(event): 
    if event.photo: 
        saved_path = await event.download_media('./img')
        await client.send_message(MY_CHANNEL, event.text, file=saved_path)
        print(saved_path)

@client.on(events.NewMessage(CHANNEL5))
async def my_event_handler(event): 
    if event.photo: 
        saved_path = await event.download_media('./img')
        await client.send_message(MY_CHANNEL, event.text, file=saved_path)
        print(saved_path)

@client.on(events.NewMessage(MY_CHANNEL2))
async def my_event_handler(event): 
    if event.photo: 
        saved_path = await event.download_media('./img')
        await client.send_message(MY_CHANNEL, event.text + 'NEWCODE', file=saved_path)
        print(saved_path)

def process_message(event): 
    pass    

client.run_until_disconnected()