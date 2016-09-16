from telegram.ext import Updater, CommandHandler
import cred

updater = Updater(token=cred.token)

dispatcher = updater.dispatcher


def start(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text='helium human')

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


updater.start_polling()
