# Setting up Webhook
# https://api.telegram.org/bot<token>/setWebhook?url=<ngrok-url>/cbbf15d8-0421-4512-84d9-5e5d977e3aef/

from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import telebot
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from . import util

tg_bot = telebot.TeleBot(settings.TOKEN_TELEGRAM_BOT)


@api_view(['POST'])
def channel_exists(request):
    data = {
        'exists': False,
        'bot_has_perm': False,
        'message': None,
    }
    if request.data.get('channel') and request.data.get('channel').startswith('https://t.me/'):
        # Формат текста 'https://t.me/breakingmash' сплитим по t.me/ и елемент с индексом 1 и будет название канала
        channel_name = '@' + request.data.get('channel').split('t.me/')[1]
        chat = util.check_exists(tg_bot, channel_name)
        if chat and util.check_bot_permissions(tg_bot, chat.id):
            data.update({'exists': True, 'bot_has_perm': True, 'message': 'OK'})
            return Response(data, status=status.HTTP_200_OK)
        else:
            data.update({'message': 'Чат не найден или у бота недостаточно прав'})
            return Response(data, status=status.HTTP_400_BAD_REQUEST, )
    else:

        data.update({'message': 'Некорректные данные'})
        return Response(data, status=status.HTTP_400_BAD_REQUEST)



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
