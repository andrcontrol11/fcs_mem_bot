import telebot
import re
from telebot import types

bot = telebot.TeleBot("5081192958:AAHoZnjlZclLZuNWwY9FOzsH-K_6I-4Hwbs")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler(commands=['hello_father'])
def hello_father(message):
    bot.send_photo(message.chat.id,open('bkjnJe_k5aM.jpeg','rb'))

@bot.inline_handler(func=lambda query: True)
def query_text(query):
    matches = re.match(r'', query.query)
    r_pic = types.InlineQueryResultPhoto(
            id='1', title="Поздоровайтесь с Отцом!",
            photo_url="https://i.imgur.com/4KgZdlg.jpg",
            thumb_url="https://i.imgur.com/4KgZdlgb.jpeg",
            photo_width="200",
            photo_height="200"
            )
    bot.answer_inline_query(query.id, [r_pic])
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if(message.text == "fcs"):
        bot.send_message(message.chat.id, "mem")
    else:
        bot.reply_to(message, message.text)
    
bot.infinity_polling()
