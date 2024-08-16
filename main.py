import telebot

bot = telebot.TeleBot("7501578133:AAGyvjIf3eQPjPo7yzJxClYCZ6xRnorrAdc")

@bot.message_handler(commands=["start", "restart"])
def handle_start(message):
    bot.send_message(message.chat.id, "The bot has been launched")

@bot.message_handler(commands=["11"])
def handle_11(message):
    for i in range(50):
        bot.send_message(message.chat.id, "1")

@bot.message_handler(commands=["stop"])
def handle_start(message):
    bot.send_message(message.chat.id, "The bot has been stopped")

bot.polling(non_stop=True)