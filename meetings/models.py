from django.db import models
from users.models import NewUser

class Meetings(models.Model):
    topic = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    about_meeting = models.TextField()
    zoom_url = models.URLField(max_length=200)
    time =  models.TimeField(null=True)
    date = models.DateField(null=True)

    user = models.ForeignKey(NewUser,on_delete=models.CASCADE)

    