from django.core.management.base import BaseCommand
from .factory import BlogerFactory, BlogFactory, PostFactory, CommentFactory
from django_loguru.middleware import logger


class Command(BaseCommand):
    help = "Создание моков для APP blogers"

    def handle(self, *args, **options):
        if options["tomock"]:
            BlogerFactory.create_batch(10)
            BlogFactory.create_batch(5)
            PostFactory.create_batch(20)
            CommentFactory.create_batch(200)
            logger.info("Моки users создались")
        else:
            logger.debug("Такой команды нет")

    def add_arguments(self, parser):
        parser.add_argument(
            "-tm",
            "--tomock",
            action="store_true",
            default=False,
            help="Вызов моков для users",
        )
