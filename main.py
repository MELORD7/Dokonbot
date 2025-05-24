import telebot
from telebot import types
import json

TOKEN = "7854161386:AAG-ma2Hypo9Is0-WCV-wHBd6IuSuV4MUL0"
ADMIN_ID = 6006020637
DATA_FILE = "mahsulotlar.json"

bot = telebot.TeleBot(TOKEN)

bo_limlar = ["PARFYUMERIYA", "XOSTAVAR", "GULLAR", "IDISHLAR", "VELIKLAR"]

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

data = load_data()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Mahsulot qidirish")
    if message.chat.id == ADMIN_ID:
        markup.add("Mahsulot qo‘shish")
    bot.send_message(message.chat.id, "Xush kelibsiz!", reply_markup=markup) 
