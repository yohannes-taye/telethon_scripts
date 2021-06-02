from telethon import TelegramClient
from telethon import events, sync
from telethon import functions, types
# Use your own values from my.telegram.org
api_id = 5182767
api_hash = '559d7a72eee8756e2df3e4db9eeac632'


client = TelegramClient('anon', api_id, api_hash).start()


#Reply to user 
# @client.on(events.NewMessage)
# async def my_event_handler(event): 
#     if event.raw_text == "test": 
#         await event.reply("Hi"); 

# client.run_until_disconnected()


# get all the channels that I can access
channels = {d.entity.username: d.entity
            for d in client.get_dialogs()
            if d.is_channel}

print(channels)
# # The first parameter is the .session file name (absolute paths allowed)
# with TelegramClient('anon', api_id, api_hash) as client:
#     client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))