#!/usr/bin/env python3
from telethon import TelegramClient
from telethon import events, sync
from telethon import functions, types
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import errors
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
import time
import csv
import sys
import traceback
import random



# Use your own values from my.telegram.org
api_id = 5083097
api_hash = '340c485966f9a9be5ad96b9442aba70e'

client = TelegramClient('anon', api_id, api_hash).start()
counter = 266
mode = 2
users = []

chats = []
last_date = None
chunk_size = 200
groups=[]
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        print(chat.title)
        #if chat.megagroup== True:
        groups.append(chat)
    except:
        continue

# print('Choose a group to add members:')
i=0
index = -1
for group in groups:
    if("PROMOTIONS AND DISCOUNTS!!!" in group.title): 
        index = i
        break
    # print(str(i) + '- ' + group.title)
    i+=1

# g_index = input("Enter a Number: ")
# target_group=groups[int(g_index)]
target_group=groups[int(index)]


target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)

# mode = int(input("Enter 1 to add by username or 2 to add by ID: "))
mode = 2
# user_to_add = client.get_input_entity('@Yefker_saw')
# client(InviteToChannelRequest(target_group_entity,[user_to_add]))
# user_to_add = InputPeerUser(575067596, -1821647138852174373)
# client(InviteToChannelRequest('https://t.me/joinchat/c0zw5lfNTak2MzA9',[user_to_add]))
with open('members.csv', newline='') as csvfile: 
    memberreader = csv.reader(csvfile, delimiter=',', lineterminator='\n')
    for row in memberreader: 
        user = {}
        
        try: 
            user['username'] = row[0]
            user['id'] = int(row[1])
            user['access_hash'] = int(row[2])
            user['name'] = row[3]
            users.insert(0, user)
            
        except ValueError: 
            continue 

n = 0
flag = 0
for user in users:
    if flag == 0 and user['id'] != 1368838274: 
        continue 
    else:
        flag = 1

    n += 1
    if n % 50 == 0:
        time.sleep(900)
    try:
        print ("Adding {}, {}".format(user['id'], user['username']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Invalid Mode Selected. Please Try Again.")
        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
        print("Waiting for 60-180 Seconds...")
        time.sleep(random.randrange(60, 180))
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except:
        traceback.print_exc()
        print("Unexpected Error")
        continue


