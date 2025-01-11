import requests
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from settings import *
from details.handlers import *

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def register_handlers():

    dispatcher.add_handler(CommandHandler("start", start)),
    dispatcher.add_handler(MessageHandler(Filters.text("Ortga🔙"), back)),
    dispatcher.add_handler(MessageHandler(Filters.text("Bot haqida📊"), stats)),
    dispatcher.add_handler(MessageHandler(Filters.text("Daraja📊"), stats)),
    dispatcher.add_handler(MessageHandler(Filters.text, text_y)),
    dispatcher.add_handler(MessageHandler(Filters.document, adding_func)),
    
    updater.start_polling()
    updater.idle()
register_handlers()