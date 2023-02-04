import uuid
from django.db import models
import administration.models as am
from faculty.models import Department
from committee.models import Committee

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
    


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False)
    capacity = models.IntegerField()
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    class_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    committee_id = models.ForeignKey(Committee, on_delete=models.CASCADE)

    def __str__(self):
        return self.title