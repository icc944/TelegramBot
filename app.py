from logging import exception
from pprint import pprint
from flask import Flask,render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL
from package.library.config import config, TOKEN
from package.library import utilities as utl
import telebot

mybot = telebot.TeleBot(TOKEN)



@mybot.message_handler(commands=['start'])
def send_welcome(message):
    mybot.reply_to(message, "¡Hola que tranza!, ¿Que puedo hacer por ti?");

@mybot.message_handler(commands=['help'])
def send_help(message):
    mybot.reply_to(message, """
    Puedes usar:\n
    \help: Para ayuda\n
    \hora: Para que te diga la hora\n
    Nomas eso se hacer por ahora unu
    """);

@mybot.message_handler(commands=['hora'])
def send_hora(message):
    # Fecha
    now = utl.get_now()
    mybot.reply_to(message, now);

@mybot.message_handler(func=lambda message: True)
def echo_all(message):
    mybot.reply_to(message, message.text);

# Saber que chat envio el mensaje y enviarle un archivo excel
@mybot.message_handler(commands=['send_data'])
def send_data(message):
    chat_id = message.chat.id;
    data = open('c:/user/carpeta/data.xlsx','rb')
    mybot.send_document(chat_id, data);
    mybot.reply_to(message, "¡Listo!");
    
bot.polling();
