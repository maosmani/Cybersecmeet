from django.db import models
from users.models import NewUser

class Meetings(models.Model):
    MY_Field = (
        ('electronic', 'electronic'),
        ('computer', 'computer'),
        ('economic', 'economic'),
        )
    field = models.CharField(max_length=100, choices=MY_Field,default = 'choose your field')
    topic = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    about_meeting = models.TextField(max_length=500)
    zoom_url = models.URLField(max_length=200)
    time =  models.TimeField(null=True)
    date = models.DateField(null=True)
   

    user = models.ForeignKey(NewUser,on_delete=models.CASCADE)

