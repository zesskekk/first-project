import telebot
bot = telebot.TeleBot('8030316710:AAFp8_EHSl9V4OjAm15zoHgsrf1ru4TrlgE')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":    
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Ты можешь написать "Привет", "Как дела?", "Хорошо", "Плохо".")
    elif message.text == "ыыы":
        bot.send_message(message.from_user.id, "не пиши мне непонятные символы")
    elif message.text == "Как дела?":
        bot.send_message(message.from_user.id, "Всё отлично! У тебя как?")
    elif message.text == "Хорошо":
        bot.send_message(message.from_user.id, "Хорошо, что хорошо:)")
    elif message.text == "Плохо":
        bot.send_message(message.from_user.id, "Жалко:(")   
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)
