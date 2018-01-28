from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def start(bot, update):
	update.message.reply_text(
		'Hola, soy Manolito, tu bot favorito :)')

updater = Updater('455286497:AAH7LZcEHYaB4X2eo_RoM7rqz7OGve1dB3I')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('holamundo', hello))

updater.start_polling()
updater.idle()
