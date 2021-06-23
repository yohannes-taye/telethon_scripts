#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://git.io/JOmFw.
"""
import logging
from UserState import UserState
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Filters, MessageHandler, Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from io import BytesIO
import random
import string
import cv2 as cv




logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
name = 'NOT CHANGED'
userStates = {}


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    global userStates
    chatId = update.message.chat_id
    if(not str(chatId) in userStates): 
        logger.info('NEW USER STATE CREATED')
        userStates[str(chatId)] = UserState(chatId)
    

    keyboard = [
        [
            InlineKeyboardButton("SCAN QR CODE", callback_data='1'),
            InlineKeyboardButton("INFO", callback_data='2'),
            InlineKeyboardButton("CANCLE", callback_data='3'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    global userStates
    query = update.callback_query
    chatId = getChatId(update)
    print(chatId)
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    if(int(query.data) == 1): 

        if(str(chatId) in userStates):
            currentState = userStates[str(chatId)] 
            if currentState.page == UserState.START: 
                userStates[str(chatId)].nextPage()
                logger.info('REQUESTING QR CODE')
                query.edit_message_text(text="Please take a picture of the Qr code so that its flat and send it to me")
        else:
            logger.INFO('USER STATE DOES NOT EXIST') 
            query.edit_message_text(text="Type /start to start using the service")
        
    if(int(query.data) == 2): 
        query.edit_message_text(text="Hello there, you can use this bot to order food from this resturant.")
    if(int(query.data) == 3): 
        query.edit_message_text(text="Thank you for using our service. Please type /start to start again")


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")

def cancelCommand(update: Update, context: CallbackContext) -> None:
    global userStates
    chatId = getChatId(update)
    userStates.pop(f'{chatId}', None)
    update.message.reply_text("Thank you for using our service. You are welcome to come back anytime /start.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1714931946:AAHbh6U7xJWwR-5jRirBSC8joUe6TFiEX3g")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('cancel', cancelCommand))
    photo_handler = MessageHandler(Filters.photo, photo)
    updater.dispatcher.add_handler(photo_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

def getChatId(update):
    chat_id = -1
    if update.message is not None:
        # from a text message
        chat_id = update.message.chat.id
    elif update.callback_query is not None:
        # from a callback message
        chat_id = update.callback_query.message.chat.id
    return chat_id

def getQrCode(qrCodeAdress): 
    logger.info("ATTEMPTING TO READ QR CODE")
    im = cv.imread(qrCodeAdress)
    det = cv.QRCodeDetector()
    retval, points, straight_qrcode = det.detectAndDecode(im)
    print('retval: {}'.format(retval))

def photo(update: Update, context: CallbackContext):
    
    global userStates
    chatId = getChatId(update)
    currentState =  userStates[str(chatId)] if str(chatId) in userStates else None
 
    if not currentState == None and currentState.getPage() == UserState.SEND_QR_CODE: 
        logger.info('IMAGE RECIEVED')
        letters = string.ascii_lowercase
        fileName = ''.join(random.choice(letters) for i in range(10))
        logger.info(f'Attempting to download')
        logger.info('ATTEMPTING TO DOWNLOAD IMAGE')
        file = context.bot.get_file(update.message.photo[-1].file_id)
        logger.info(f'Downloading to location ./img2/{fileName}.jpg')
        file.download(f'./img2/{fileName}.jpg')
        logger.info('IMAGE DOWNLOADED SUCCESSFULLY')
        userStates[str(chatId)].setQrCodeAdress('./img2/{fileName}.jpg')
        userStates[str(chatId)].nextPage()
        getQrCode('./img2/{fileName}.jpg') 
    elif currentState == None:
        #TODO: send message saying that they should start by typing /start
        context.bot.send_message(chat_id=update.message.chat_id, text="Please start by typing /start")
        
if __name__ == '__main__':
    main()
