import uuid
from django.db import models
from administration.models import Room 

# Create your models here.


class Slot(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    name = models.CharField(max_length=5, blank=True)
    start_time = models.TimeField()


class RoomCalendar(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    slot =models.ForeignKey(Slot,on_delete=models.CASCADE)