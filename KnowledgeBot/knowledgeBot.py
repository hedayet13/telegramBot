import os
import telebot
import logging
import wikipedia as wiki

API_KEY = '1794714841:AAH4iAcEZzZFK08aAOMkzeSgHJ7MKQVvuq4'
# API_KEY = os.getenv('API_KEY')
bot=telebot.TeleBot(API_KEY)
logger= telebot.logger


@bot.message_handler(commands=['hello','greet'])
def hello(message):
    bot.reply_to(message,'Hey guyz')


@bot.message_handler(func=lambda message:True)
def echo_all(message):
    z = wiki.summary(message)
    bot.reply_to(message,z.text)


# @bot.callback_query_handler(func=lambda call:True)
# def test_callback(call):
#     logger.info(call)

bot.polling()