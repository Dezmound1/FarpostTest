from django.core.management.base import BaseCommand
from logs.models import SpaceType, EventType
from .factory import LogsFactory
from django_loguru.middleware import logger


class Command(BaseCommand):
    help = "Создание базовых записей для SpaceType и EventType"

    def handle(self, *args, **options):
        spaces = ["global", "blog", "post"]
        events = ["login", "comment", "create_post", "delete_post", "logout"]

        for space in spaces:
            SpaceType.objects.get_or_create(name=space)

        for event in events:
            EventType.objects.get_or_create(name=event)

        logger.info("Базовые моки logs созданы")

        for _ in range(26):
            LogsFactory()
        logger.info("Моки logs создались")
