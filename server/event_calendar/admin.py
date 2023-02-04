from django.contrib import admin
from event_calendar.models import RoomCalendar, Slot

# Register your models here.
admin.site.register(RoomCalendar)
admin.site.register(Slot)
