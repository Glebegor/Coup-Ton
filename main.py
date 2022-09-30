from email.headerregistry import AddressHeader
import telebot 
from telebot import types
import logging
from flask import Flask, request
import os

TOKEN = "5775775773:AAH84S2Etu_YsbQ4eAwy05gwPxZ1gLIsXN4"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_start(message):
    bot.send_message(message.chat.id, "Main")

if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)   
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://tonanabot.herokuapp.com/")
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    bot.remove_webhook()
    bot.polling(none_stop=True)