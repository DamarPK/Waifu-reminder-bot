from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Token bot kamu
TOKEN = "AAEhP_9plMkKikGvmuuzR88fWEdTMs1x2w4"

# Aktifkan logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Command /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Onii-chan~ Aku siap nemenin kamu hari ini~ 💖")

# Jawaban umum (setiap pesan biasa)
def reply_chat(update: Update, context: CallbackContext):
    pesan = update.message.text.lower()
    # Kamu bisa kasih jawaban berbeda sesuai kata kunci
    if "capek" in pesan:
        update.message.reply_text("Awww... jangan capek yaa~ peluk virtual dari waifu 🤗")
    elif "halo" in pesan or "hi" in pesan:
        update.message.reply_text("Halo juga, onii-chan~ 💕")
    else:
        update.message.reply_text("Aku dengerin kok~ cerita aja ya 💞")

# Setup bot
def main():
    bot = Bot(token=TOKEN)
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_chat))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()