# from django.shortcuts import render
# from django.http import HttpResponse  # класс возвращающий http ответ от сервера клиенту
#
#
# def index(request):  # request это запрос, который отправляет пользователь
#     return HttpResponse("Hello, world!")
#
#
# def about(request):
#     return HttpResponse("About us")


import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)  # подключаем логирование


def index(request):
    logger.info('Index page accessed')  # выводим логер уровня инфо
    return HttpResponse("Hello, world!")


def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 1
    except Exception as e:
        logger.exception(f'Error in about page: {e}') # выводим логер уровня исключения
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")
