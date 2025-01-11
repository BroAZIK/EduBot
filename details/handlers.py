from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Bot, InputMediaPhoto, InputMediaVideo
from telegram.ext import CallbackContext
from telegram.parsemode import ParseMode
from pprint import pprint
from .messages import *
from .buttons import *
from settings import *
from database.db import *
import json

def start(update: Update, context):
    user_id = update.effective_chat.id
    first = update.effective_chat.first_name

    if user_id == ADMIN_ID:
        update.message.reply_text(
            text=admin_start,
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=ReplyKeyboardMarkup(admin_start_but, resize_keyboard=True)
        )
    else:
        update.message.reply_text(
            text=start_mes.format(first),
            parse_mode=ParseMode.HTML,
            reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True)
        )
        update.message.reply_text(
            text=start_mes2.format(first),
            parse_mode=ParseMode.HTML,
            reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True)
        )
    try: 
            insert(table="index",user_id=update.message.chat.id, data={
            "Stage": "start",
            "Essential": 0,
            "Essential2": 0,
            "ELS": 0,
            })

    except:
            upd(table="index",user_id=update.message.chat.id, data={
                "Stage": "start",
                "Essential1": 0,
                "Essential2": 0,
                "ELS": 0,
                })

def text_y(update: Update, context):
    user_id = update.effective_chat.id
    message = update.message.text

    if message == "Essential1":
        upd(table='index', user_id=user_id, data={"Stage": "Essential1"})
        update.message.reply_text(
            text="Essential1 qo'shish uchun .JSON fayl kutilmoqda ... ",
            reply_markup=ReplyKeyboardMarkup(ortga_but, resize_keyboard=True)
        )
    elif message == "Essential2":
        upd(table='index', user_id=user_id, data={"Stage": "Essential2"})
        update.message.reply_text(
            text="Essential2 qo'shish uchun .JSON fayl kutilmoqda ... ",
            reply_markup=ReplyKeyboardMarkup(ortga_but, resize_keyboard=True)
        )
    elif message == "ELS":
        upd(table='index', user_id=user_id, data={"Stage": "ELS"})
        update.message.reply_text(
            text="ELS qo'shish uchun .JSON fayl kutilmoqda ... ",
            reply_markup=ReplyKeyboardMarkup(ortga_but, resize_keyboard=True)
        )

def adding_func(update: Update, context):
    user_id = update.effective_chat.id
    
    if user_id == ADMIN_ID:
        case = get(table="index", user_id=user_id)['Stage']
        if not update.message or not update.message.document:
            update.message.reply_text("Iltimos, faqat .json formatdagi fayl yuboring.")
            return
        document = update.message.document

        if not document.file_name.endswith('.json'):
            update.message.reply_text("Xato! Faqat .json fayllarini yuboring.")
            return

        try:
            file = context.bot.get_file(document.file_id)
            file_path = os.path.join(os.getcwd(), "temp.json")
            file.download(file_path)

            with open(file_path, 'r', encoding='utf-8') as f:
                dictionary_data = json.load(f)

            os.remove(file_path)

            result = insert(table=case, data=dictionary_data)
            update.message.reply_text(result)
        except json.JSONDecodeError:
            update.message.reply_text("Xato! JSON fayl noto‘g‘ri formatda.")
        except Exception as e:
            update.message.reply_text(f"Xatolik yuz berdi: {e}")

def back(update: Update, context):
    user_id = update.message.chat.id

    upd(table="index", user_id=user_id, data={"Stage": "start"})
    if user_id != ADMIN_ID:
        update.message.reply_text(
            text=ortga_mes,
            reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True)
        )

    else:
        update.message.reply_text(
            text=ortga_mes,
            reply_markup=ReplyKeyboardMarkup(admin_start_but, resize_keyboard=True)
        )

def stats(update, context):
    users = len(db1.table("Index"))
    dictionary = len(db2)
    upd(table="index",user_id=update.message.chat.id, data={"Stage": "start"})
    if ADMIN_ID == update.message.chat.id:
        update.message.reply_text(text=stats_mes.format(users, dictionary), parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardMarkup(admin_start_but, resize_keyboard=True))
    else:
        update.message.reply_text(text=stats_mes.format(users, dictionary), parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True))