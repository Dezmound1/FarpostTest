import factory
from factory.django import DjangoModelFactory
from logs.models import Logs, EventType, SpaceType
from django.utils import timezone

spaces = ["global", "blog", "post"]
events = ["login", "comment", "create_post", "delete_post", "logout"]


class SpaceTypeFactory(DjangoModelFactory):
    class Meta:
        model = SpaceType

    name = factory.Iterator(spaces)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        obj, created = model_class.objects.get_or_create(**kwargs)
        return obj


class EventTypeFactory(DjangoModelFactory):
    class Meta:
        model = EventType

    name = factory.Iterator(events)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        obj, created = model_class.objects.get_or_create(**kwargs)
        return obj


class LogsFactory(DjangoModelFactory):
    class Meta:
        model = Logs

    datetime = factory.LazyFunction(timezone.now)
    user_id = factory.Sequence(lambda n: n + 1)
    space_type_id = factory.SubFactory(SpaceTypeFactory)
    event_type_id = factory.SubFactory(EventTypeFactory)

    @factory.post_generation
    def adjust_space_and_event(obj, create, extracted, **kwargs):
        if obj.event_type_id.name in ["login", "logout"]:
            obj.space_type_id = SpaceType.objects.filter(name="global").first()
        elif obj.event_type_id.name in ["create_post", "delete_post"]:
            obj.space_type_id = SpaceType.objects.filter(name="blog").first()
        elif obj.event_type_id.name == "comment":
            obj.space_type_id = SpaceType.objects.filter(name="post").first()
        obj.save()
