import uuid
from django.db import models
import administration.models as am

# Create your models here.


class Slot(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    name = models.CharField(max_length=5, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return "{} {} - {}".format(self.name,self.start_time,self.end_time)


class RoomCalendar(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    room = models.ForeignKey(am.Room,on_delete=models.CASCADE)
    date = models.DateField(blank=False)
    slot = models.ForeignKey(Slot,on_delete=models.CASCADE)
    event = models.ForeignKey(am.Event,on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {}".format(self.room,self.date,self.slot,self.event)

class Holiday(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    date = models.DateField(blank=False)

    def __str__(self):
        return str(self.date)