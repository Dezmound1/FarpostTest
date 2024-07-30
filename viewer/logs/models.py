from django.db import models

class EventType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "event_type"
        app_label = "logs"

class SpaceType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "space_type"
        app_label = "logs"

class Logs(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
    space_type_id = models.ForeignKey(SpaceType, on_delete=models.CASCADE)
    event_type_id = models.ForeignKey(EventType, on_delete=models.CASCADE)

    class Meta:
        db_table = "logs"
        app_label = "logs"
