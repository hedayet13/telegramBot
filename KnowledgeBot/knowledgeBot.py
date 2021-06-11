import os
import telebot
import logging
import wikipedia as wiki
import wikipediaapi

API_KEY = '1794714841:AAH4iAcEZzZFK08aAOMkzeSgHJ7MKQVvuq4'
# API_KEY = os.getenv('API_KEY')
bot=telebot.TeleBot(API_KEY)
logger= telebot.logger
wikiapi =wikipediaapi.Wikipedia('en')

@bot.message_handler(commands=['hello','greet'])
def hello(message):
    bot.reply_to(message,'Hey guyz')


@bot.message_handler(func=lambda message:True)
def echo_all(message):
    page_py= wikiapi.page(message.text)
    if page_py.exists()==True:
        # url = page_py.fullurl
        msg = page_py.summary
        z=msg.split('.')
        z=z[:5]
        z=".".join(z)
        # if len(src)!=0:
        #     msg=src[0]
        #     z = wiki.summary(msg)
        #     z = z.split('.')
        #     z = z[:5]
        #     z = ".".join(z)
        bot.send_message(message.chat.id,z)
        bot.send_message(message.chat.id,page_py.fullurl)
        #Todo Add Url for read more
    else:
        bot.send_message(message.chat.id,"Page Doesn't exit")

    # bot.reply_to(message,z)


# @bot.callback_query_handler(func=lambda call:True)
# def test_callback(call):
#     logger.info(call)

bot.polling()