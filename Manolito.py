from telegram.ext import Updater, CommandHandler
from WebSearch import find
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

def pelicula(bot, update, args):
	update.message.reply_text('Estoy buscando...')
	res = ""
	for i in args:
		res = res +' '+ i
	update.message.reply_text(res)
	dict = find(res, 0)
	update.message.reply_text('Esto es lo que he encontrado')
	for key in dict:
		update.message.reply_text(dict[key])



updater = Updater('455286497:AAH7LZcEHYaB4X2eo_RoM7rqz7OGve1dB3I')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('holamundo', hello))
updater.dispatcher.add_handler(CommandHandler('fecha', obtener_hora))
updater.dispatcher.add_handler(CommandHandler('buscarpeli', pelicula, pass_args=True))

updater.start_polling()
updater.idle()
