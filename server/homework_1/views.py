# Создайте пару представлений в вашем первом приложении:
# главная и о себе.
# Внутри каждого представления должна быть переменная html - многострочный текст с HTML вёрсткой и данными о
# вашем первом Django сайте и о вас.
# *Сохраняйте в логи данные о посещении страниц

from django.shortcuts import render
from django.http import HttpRequest
import logging


logger = logging.getLogger(__name__)


def index(request: HttpRequest):
    logger.info('Index page get request')
    return render(request, 'index.html')


def about(request: HttpRequest):
    logger.info('Аbout page get request')
    return render(request, 'about.html')
