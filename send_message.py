#!/usr/bin/env python3
from telethon import TelegramClient
from telethon import events, sync
from telethon import functions, types
# Use your own values from my.telegram.org
api_id = 5182767
api_hash = '559d7a72eee8756e2df3e4db9eeac632'


client = TelegramClient('anon', api_id, api_hash).start()

client.send_message('me', 'Hello! Talking to you from Telethon', file='./img/img1.jpg')
# await client.send_file('me', './img/img1.jpg')
 