from email.headerregistry import AddressHeader
import telebot 
from telebot import types
import logging
from flask import Flask, request
import os

TOKEN = "5763220019:AAFT3EDWId5ZiHqGBkQxF5M-qjyZ6KQPOBM"

bot = telebot.TeleBot(TOKEN)

bot.set_my_commands([
    types.BotCommand('/start', "Start bot"),
    types.BotCommand('/menu', "menu of bots"),
    types.BotCommand('/info', "Information"),
])


@bot.message_handler(commands=["start"])
def send_start(message):
    

    bot.send_message(message.chat.id, "Hello!✋ \nThis bot created what would you and your friends will have a fun!\n(😊and some money😊)\nIt's place for a couple on something sport\nOpen /menu to see navigation\nAnd click /info to see information")

@bot.message_handler(commands=["info"])
def send_start(message):
    bot.send_message(message.chat.id, "Information about bot.\n\nAt the first you need to connect your 💎wallet💎.\nAfter create room you need choise match of your ⚽️sport⚽️(if your friend create room, you will need connect to him with code of room) and set bet in Ton. ")

@bot.message_handler(commands=["menu"])
def send_start(message):
    bot.send_message(message.chat.id, "I can give you fun with your friends.\n\n/info - Information about bot\n/ConRoom - Connect to the room ")

@bot.message_handler(commands=["ConRoom"])
def send_start(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    webapp = types.WebAppInfo(url="https://staging.agorapp.dev/editor/courses/solidity/1/1")
    markup.add(types.InlineKeyboardButton(text="Rooms", web_app=webapp))
    bot.send_message(message.chat.id, "Connect to rooms", reply_markup=markup)

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