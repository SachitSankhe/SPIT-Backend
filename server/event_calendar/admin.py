from django.contrib import admin
import event_calendar.models as em

# Register your models here.
admin.site.register(em.RoomCalendar)
admin.site.register(em.Slot)
admin.site.register(em.Holiday)
admin.site.register(em.Room)
