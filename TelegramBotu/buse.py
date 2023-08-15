import os
import telebot
import requests

# Bot Token
BOT_TOKEN = '6476379587:AAHV8k4JiVUrhRgMwCzLz8YqMWzSoYbCbpU'
url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'

response = requests.get(url)
data = response.json()

if 'result' in data:
    for update in data['result']:
        chat_id = update['message']['chat']['id']
        print(f"Chat ID: {chat_id}")
# Buse kendisine daha önce mesaj göndermiş kullanıcılara mesaj gönderebilmektedir 12-15. satır aralığındaki kod bloğu daha önce mesaj gönderen kullanıcıların Chat ID'Sine erişmeyi sağlar.
# Buse'nin sürekli olarak çalışabilmesi için sanal makine kullanımı gerekmektedir.
ip_address = '89.19.29.128'

# Create Telebot Object
bot = telebot.TeleBot(BOT_TOKEN)

# Send IP Connection Message
ip_message = f"Bot IP'ye bağlandı: {ip_address}"

# Whenever Starting Bot
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    # Inline Button
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Patron'a ulaşın", url="https://web.telegram.org/k/#@dodooo_oo"))

    markdown = f"""Selamlar *{message.chat.first_name}* ben Telegram Botu Buse 😁.\n\n Nasıl yardımcı olabilirim ?"""

    bot.reply_to(message, markdown, parse_mode="Markdown", reply_markup=markup)
    print(f"Hoşgeldiniz mesajı {message.chat.first_name} Kişisine gönderildi.\n\n")


# Handle Documents
@bot.message_handler(func=lambda m: True, content_types=['document'])
def handle_docs_photo(message):
    if message.document:
        bot.reply_to(message, f"Üzgünüm {message.chat.first_name}, belge türünü desteklemiyorum.")
        print(f"Mesaj {message.chat.first_name} Kişisine gönderildi.\n")
    elif message.photo:
        bot.reply_to(message, f"Üzgünüm {message.chat.first_name}, fotoğraf türünü desteklemiyorum.")
        print(f"Mesaj {message.chat.first_name} Kişisine gönderildi.\n")

user_chat_ids = {}


# Reply To All Messages
@bot.message_handler(func=lambda msg: True)
def all(message):
    user_chat_ids[message.from_user.username] = message.chat.id
    bot.reply_to(message, f"Üzgünüm {message.chat.first_name}, ben henüz geliştirilme aşamasındayım.")
    print(f"Mesaj {message.chat.first_name} Kişisine gönderildi.\n")

    # Extract the text after the command
    command_args = message.text.split(None, 1)
    if len(command_args) > 1:
        message_text = command_args[1]

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        params = {
            "chat_id": "@deniz111111",
            "text": "Merhaba! Ben Buse, Telegram botu."
        }
        response = requests.post(url, data=params)

        if response.status_code == 200:
            bot.reply_to(message, "Mesajınız başarıyla gönderildi!")
        else:
            bot.reply_to(message, "Mesaj gönderilirken bir hata oluştu.")
    else:
        bot.reply_to(message, "Gönderilecek mesajı belirtmelisiniz.")

    # Send a message to a specific chat
    bot.send_message("@deniz111111", "Merhaba! Ben Buse, Telegram botu.")

    bot.send_message("@deniz111111", ip_message)






print("Bot çalışıyor, mesajlar gönderilebilir.\n")

# Waiting For New Messages
bot.infinity_polling()
