import telebot
from telebot import types
import fonts

bot = telebot.TeleBot('7898724214:AAGgH0fMtTpAeCjduzGFE8tEDaYKCHdzsu8')
t_font = 0

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global t_font
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши что нибудь, и я переведу это на эльфийский, для смены шрифта используй команду /change_font")
        
    elif message.text == "/change_font":
        keyboard = types.InlineKeyboardMarkup() 
        key_ch = types.InlineKeyboardButton(text='Кит', callback_data='chinese')
        keyboard.add(key_ch) 
        key_funny= types.InlineKeyboardButton(text='Другое', callback_data='funny')
        keyboard.add(key_funny)
        
        question = 'Какой шрифт использовать?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
               
        
    else:
        if t_font == 1:
            bot.send_message(message.from_user.id, fonts.to_funny_font(message.text.lower()))
        elif t_font == 0:
            bot.send_message(message.from_user.id, fonts.to_chinese_font(message.text.lower()))





@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global t_font
    
    if call.data == "chinese":
        t_font = 0
    elif call.data == "funny":
        t_font = 1
    
    bot.send_message(call.message.chat.id, 'Запомню : )')



bot.polling(none_stop=True, interval=0)