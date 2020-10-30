# Setting up Webhook
# https://api.telegram.org/bot<token>/setWebhook?url=<ngrok-url>/cbbf15d8-0421-4512-84d9-5e5d977e3aef/
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import telebot

tg_bot = telebot.TeleBot(settings.TOKEN_TELEGRAM_BOT)


@csrf_exempt
def channel_exists(request):
    if request.method == 'POST':
        if request.POST.get('channel').startswith('https://t.me/'):
            # Формат текста 'https://t.me/breakingmash' сплитим по t.me/ и елемент с индексом 1 и будет название канала
            channel_name = request.POST['channel'].split('t.me/')[1]
            try:
                chat_data = tg_bot.get_chat(f'@{channel_name}')
                return JsonResponse(chat_data, status=status.HTTP_200_OK, safe=False,)
            except Exception as e:
                data = {
                    'message': 'Чат не найден'
                }
                return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST, json_dumps_params={'ensure_ascii': False})
        else:
            data = {
                'message': 'Некорректные данные'
            }
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST, json_dumps_params={'ensure_ascii': False})
    else:
        data = {
            'message': 'Доступ'
        }
        return JsonResponse(data, status=status.HTTP_403_FORBIDDEN, json_dumps_params={'ensure_ascii': False})


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
