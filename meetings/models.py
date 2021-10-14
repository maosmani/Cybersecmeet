from django.db import models
from users.models import NewUser

class Meetings(models.Model):



    topic = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    about_meeting = models.TextField(max_length=500)
    zoom_url = models.URLField(max_length=200)
    zoom_password = models.CharField(max_length=250)
    time =  models.TimeField(null=True)
    date = models.DateField(null=True)
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE, default = 1)

    def __str__(self):
        return self.field
  


class StudentMeetings(models.Model):
    meetings = models.ForeignKey(Meetings,on_delete=models.CASCADE, default = 1)
    new_user = models.ForeignKey(NewUser, on_delete=models.CASCADE, default = 1)



