import telebot
import requests
from telebot.types import InlineKeyboardButton as Btn , InlineKeyboardMarkup as Mak

token = "6715220090:AAGnTUEUKu1fYPSXbNdgXieNMD5Ly77W9NI"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
  name = message.from_user.first_name
  bot.reply_to(message,'''مرحباً {}
• بـوت تحميل من التيك توك ارسـل
الان رابـط لتحميل 📍. 
'''.format(name)) 

@bot.message_handler(func=lambda brok:True)
def Url(message):
    try:
      msgg = bot.send_message(message.chat.id, "🚀",parse_mode="markdown")
      msg = message.text
      url = requests.get(f'https://tikwm.com/api/?url={msg}').json()
      music = url['data']['music']
      region = url['data']['region']
      tit = url['data']['title']
      vid = url['data']['play']
      ava = url['data']['author']['avatar']
      ##
      name = url['data']['music_info']['author']
      time = url['data']['duration']
      sh = url['data']['share_count']
      com = url['data']['comment_count']
      wat = url['data']['play_count']
      bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
      bot.send_photo(message.chat.id,ava,caption=f'- اسم الحساب : *{name}*\n - دوله الحساب : *{region}*\n\n- عدد مرات المشاهدة : *{wat}*\n- عدد التعليقات : *{com}*\n- عدد مرات المشاركة : *{sh}*\n- طول الفيديو : *{time}*',parse_mode="markdown")
      btn = Mak().add(Btn('تحميل الصوت ❤️‍🔥',url=''+music))
      bot.send_video(message.chat.id,vid, caption=f"{tit}",reply_markup=btn)
    except:
      pass
      bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
      bot.reply_to(message,'🔴|| خطأ تأكد من الرابط 💀.')


print('run')
bot.infinity_polling()
