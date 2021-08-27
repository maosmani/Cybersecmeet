from django.contrib import admin
from .models import Meetings
from .models import StudentMeetings

admin.site.register(Meetings)
admin.site.register(StudentMeetings)

# Register your models here.
