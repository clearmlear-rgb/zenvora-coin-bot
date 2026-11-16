
import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "💎 Welcome to ZENVORA COIN!\n\n"
        "🚀 Start earning ZENVORA.\n\n"
        "⛏ Mining\n"
        "👛 Wallet\n"
        "👥 Referral\n"
        "💰 Balance"
    )

@bot.message_handler(commands=["balance"])
def balance(message):
    bot.reply_to(message, "💎 Your ZENVORA balance: 0")

bot.infinity_polling()
