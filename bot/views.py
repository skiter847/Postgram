# Setting up Webhook
# https://api.telegram.org/bot<token>/setWebhook?url=<ngrok-url>/cbbf15d8-0421-4512-84d9-5e5d977e3aef/

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import telebot

tg_bot = telebot.TeleBot(settings.TOKEN_TELEGRAM_BOT)



@csrf_exempt
def update(request):
    """ Сюда попадают все новые апдейты, после чего боту отдаеться этот апдейт в хендлеры """
    if request.META['CONTENT_TYPE'] == 'application/json':

        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        tg_bot.process_new_updates([update])

        return HttpResponse("")

    else:
        return HttpResponse("403")


@tg_bot.message_handler(commands=['start'])
def start_message(message):
    tg_bot.send_message(message.chat.id, 'hello')
