import telebot
import json
import os
import random

# توکن رباتت رو اینجا بذار
TOKEN = '8082409003:AAGXKj-aADBiC85Cm0wFAeb_KYSsHrq0-DI'
bot = telebot.TeleBot(TOKEN)

# تابع برای گرفتن مسیر فایل دیتابیس کاربر
def get_user_file(user_id):
    return f'user_{user_id}.json'

# تابع برای لود کردن داده‌های کاربر
def load_user_data(user_id):
    file_path = get_user_file(user_id)
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"فایل JSON برای کاربر {user_id} خراب است.")
            return {'wins': 0, 'losses': 0, 'draws': 0}
    return {'wins': 0, 'losses': 0, 'draws': 0}

# تابع برای ذخیره داده‌های کاربر
def save_user_data(user_id, data):
    file_path = get_user_file(user_id)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_as
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    web_app = telebot.types.WebAppInfo('https://sissmaison.ir/')  # URL واقعی مینی اپت رو بذار
    keyboard.add(telebot.types.InlineKeyboardButton('شروع بازی دوز', web_app=web_app))
    bot.reply_to(message, 'سلام! بیا با هم دوز بازی کنیم. دکمه زیر رو بزن:', reply_markup=keyboard)

# هندلر برای دریافت داده از مینی اپ
@bot.message_handler(content_types=['web_app_data'])
def web_app_data(message):
    user_id = message.from_user.id
    try:
        data = json.loads(message.web_app_data)
        result = data.get('result')  # نتیجه بازی: win, loss, draw
        user_data = load_user_data(user_id)
        if result == 'win':
            user_data['wins'] += 1
            bot.reply_to(message, 'آفرین! تو بردی! 🎉')
        elif result == 'loss':
            user_data['losses'] += 1         bot.reply_to(message, 'اووه، من بردم! 😎 دوباره امتحان کن.')
        elif result == 'draw':
            user_data['draws'] += 1
            bot.reply_to(message, 'تساوی شد! 🤝 یه دست دیگه بریم؟')
        save_user_data(user_id, data)
        # نمایش امتیازات
        bot.reply_to(message, f'امتیازاتت: بردها: {user_data["wins"]}، باخت‌ها: {user_data["losses"]}، تساوی: {user_data["draws"]}')
    except Exception as e:
        bot.reply_to(message, 'مشکلی پیش اومد! دوباره امتحان کن.')
        print(f"Error: {e}")

# اجرای ربات
try:
    bot.polling(none_stop=True, timeout=30)
except Exception as e:
    print(f"Error: {e}")
    import time
    time.sleep(10)
    bot.polling(none_stop=True, timeout=30)


    =====-p0ppppo987yuop=====-0o9i888[ppp