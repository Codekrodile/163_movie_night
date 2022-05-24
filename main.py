import telebot
import quiz

# import config
# API_KEY = config.API_KEY

import os
from flask import Flask, request
API_KEY = os.environ.get("API_KEY", None)
server = Flask(__name__)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(msg):
    text = "welcome to movie night quiz bot!!! \nRules are simple, answer 3 quiz correctly in a row to redeem a prize! Fail one quiz and you'll have to start all over:( \ntype /quiz to get started:)"

    bot.send_message(msg.chat.id, text)

@bot.message_handler(commands=['quiz'])
def quiz_1(msg):
    qn, ans, options = quiz.quiz(1)
    print(qn, ans, options)
    text = "QUIZ QUESTION 1: QUICK MATH\n\n" + qn

    keyboard = telebot.types.InlineKeyboardMarkup()
    for i in options:
        if i != ans:
            keyboard.row(telebot.types.InlineKeyboardButton(i, callback_data=f"fail_{ans}"))
        else:
            keyboard.row(telebot.types.InlineKeyboardButton(i, callback_data="quiz_2"))

    bot.send_message(msg.chat.id, text, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "quiz_2")
def handle_quiz_2(call):
    bot.answer_callback_query(call.id) #required to remove the loading state, which appears upon clicking the button

    qn, ans, options = quiz.quiz(2)
    print(qn, ans, options)
    text = "QUIZ QUESTION 2: SLOW MATH\n\n" + qn

    keyboard = telebot.types.InlineKeyboardMarkup()
    for i in options:
        if i != ans:
            keyboard.row(telebot.types.InlineKeyboardButton(i, callback_data=f"fail_{ans}"))
        else:
            keyboard.row(telebot.types.InlineKeyboardButton(i, callback_data="quiz_3"))
    
    bot.edit_message_text(
        text= "Congrats! You are correct:) \n\n[can include fun facts here]",
        chat_id= call.message.chat.id,
        message_id= call.message.message_id
    )

    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "quiz_3")
def handle_quiz_3(call):
    bot.answer_callback_query(call.id) #required to remove the loading state, which appears upon clicking the button

    qn, ans, options = quiz.quiz(3)
    print(qn, ans, options)
    text = "QUIZ QUESTION 3: MOST SLOW MATH\n\n" + qn

    keyboard = telebot.types.InlineKeyboardMarkup()
    for i in options:
        if i != ans:
            keyboard.row(telebot.types.InlineKeyboardButton(i, callback_data=f"fail_{ans}"))
        else:
            keyboard.row(telebot.types.InlineKeyboardButton(i, callback_data="pass"))
    
    bot.edit_message_text(
        text= "Congrats! You are correct:) \n\n[can include fun facts here]",
        chat_id= call.message.chat.id,
        message_id= call.message.message_id
    )
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "pass")
def handle_pass(call):
    bot.answer_callback_query(call.id) #required to remove the loading state, which appears upon clicking the button

    text = "Congrats! You have made it to the end! Please show this message to the quiz booth to redeem ur prize. \nThank you and enjoy the upcoming movie:)"
    
    bot.edit_message_text(
        text= "Congrats! You are correct:) \n\n[can include fun facts here]",
        chat_id= call.message.chat.id,
        message_id= call.message.message_id
    )
    bot.send_message(call.message.chat.id, text)

@bot.callback_query_handler(func=lambda call: call.data.startswith("fail"))
def handle_fail(call):
    bot.answer_callback_query(call.id) #required to remove the loading state, which appears upon clicking the button
    
    bot.edit_message_text(
        text= f"U failed, you'll get them next time. \nCorrect ans is {call.data.split('_')[1]} \n\ntype /quiz to restart the quiz",
        chat_id= call.message.chat.id,
        message_id= call.message.message_id
    )

# bot.polling()

@server.route('/' + API_KEY, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://movienightquizbot.herokuapp.com/" + API_KEY)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
