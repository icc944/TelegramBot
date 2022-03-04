from logging import exception
from pprint import pprint
from flask import Flask,render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL
from bookstore.config import config, TOKEN
from bookstore import myDarling as md
import telebot

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola que tranza!, ¿Que puedo hacer por ti?")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """
    Puedes usar:\n
    \help: Para ayuda\n
    \hora: Para que te diga la hora\n
    Nomas eso se hacer por ahora unu
    """)

@bot.message_handler(commands=['hora'])
def send_hora(message):
    # Fecha
    now = md.get_now()
    bot.reply_to(message, now)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()