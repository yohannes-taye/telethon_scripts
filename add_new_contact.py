from telethon import TelegramClient
from telethon import events, sync
from telethon import functions, types
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import errors
import time
import csv
# Use your own values from my.telegram.org
api_id = 5083097
api_hash = '340c485966f9a9be5ad96b9442aba70e'

client = TelegramClient('anon', api_id, api_hash).start()
counter = 266
startFromUser = 'Yamelake'
startAdding = 0

with open('members.csv', newline='') as csvfile: 
    memberreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in memberreader: 
        if row[0] == startFromUser: 
            startAdding = 1
        if row and row[0] != '' and startAdding == 1: 
            print('Attempting to add @{0} to contact'.format(row[0]))
            try: 
                result = client(functions.contacts.AddContactRequest(
                    id='@' + row[0], 
                    first_name='LR' + str(counter),
                    last_name='', 
                    phone='', 
                ))
                print("\t@" + row[0] + ' added as new contact under LR' + str(counter))
            except TypeError:
                print('\tFailed to add @{0} to contact'.format(row[0]))
            
            except errors.FloodWaitError as e:
                print('Have to sleep', e.seconds, 'seconds')
                time.sleep(e.seconds)
            counter += 1 






result = client(functions.contacts.AddContactRequest(
    id='@lonelynhappy', 
    first_name='LR_TEST', 
    last_name='', 
    phone='', 
))
print(result.stringify())
# contact = InputPhoneContact(client_id=1539585601, phone='', 
#     first_name="user",
#     last_name="test")
# result = client(ImportContacatsRequest(contacts=[contact]))
# print(result.__dict__)