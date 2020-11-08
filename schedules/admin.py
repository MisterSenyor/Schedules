from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Schedule)
admin.site.register(School)
admin.site.register(ClientUser)
admin.site.register(Task)
admin.site.register(ScheduleClass)
admin.site.register(HomeroomClass)