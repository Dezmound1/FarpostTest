from django.core.management.base import BaseCommand
from logs.models import SpaceType, EventType
from .factory import LogsFactory
from django_loguru.middleware import logger
from .factory import spaces, events


class Command(BaseCommand):
    help = "Создание моков для Logs"

    def handle(self, *args, **options):

        if options["tomock"]:
            for space in spaces:
                SpaceType.objects.get_or_create(name=space)

            for event in events:
                EventType.objects.get_or_create(name=event)

            logger.info("Базовые моки logs созданы")

            for _ in range(200):
                LogsFactory()
            logger.info("Моки logs создались")
        else:
            logger.debug("Такой команды нет")

    def add_arguments(self, parser):
        parser.add_argument(
            "-tm",
            "--tomock",
            action="store_true",
            default=False,
            help="Вызов моков для logs",
        )
