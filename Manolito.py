from telegram.ext import Updater, CommandHandler
import time

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def start(bot, update):
    update.message.reply_text('¡Hola!, soy Manolito, tu bot favorito :)')


def obtener_hora(bot, update):
    meses = {'January': 'Enero', 'February': 'Febrero', 'March': 'Marzo', 'April': 'Abril', 'May':'Mayo', 'June': 'Junio',
             'July': 'Julio', 'August':'Agosto', 'September':'Septiembre', 'October':'Octubre', 'November':'Noviembre',
             'December':'Diciembre'}
    dias = {'Monday':'Lunes', 'Tuesday':'Martes', 'Wednesday':'Miércoles', 'Thursday':'Jueves', 'Friday':'Viernes',
            'Saturday':'Sábado', 'Sunday':'Domingo'}

    date = time.strftime('Son las %H:%M del %A %d de %B de %Y').split()
    #Cambiamos el día a español
    date[4] = dias[date[4]]
    #Cambiamos el mes a español
    date[7] = meses[date[7]]

    finaldate = ''
    for i in date:
        finaldate = finaldate + i + ' '

    update.message.reply_text(finaldate)


updater = Updater('455286497:AAH7LZcEHYaB4X2eo_RoM7rqz7OGve1dB3I')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('holamundo', hello))
updater.dispatcher.add_handler(CommandHandler('fecha', obtener_hora))

updater.start_polling()
updater.idle()
