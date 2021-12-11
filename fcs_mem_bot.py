import telebot

bot = telebot.TeleBot("5081192958:AAHoZnjlZclLZuNWwY9FOzsH-K_6I-4Hwbs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler(commands=['Здарова,отец!'])
def hello_father(message):
    bot.send_photo(message.chat.id,open('bkjnJe_k5aM.jpg','rb'))
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if(message.text == "fcs"):
        bot.send_message(message.chat.id, "mem")
    else:
        bot.reply_to(message, message.text)
    
bot.infinity_polling()
