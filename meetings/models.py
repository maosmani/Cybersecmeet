from django.db import models
from users.models import NewUser

class Meetings(models.Model):
    MY_Field = (
        ('Applications and Real-Time Area', 'Applications and Real-Time Area'),
        ('General Area', 'General Area'),
        ('Internet Area', 'Internet Area'),
        ('Operations and Management Area  ', 'Operations and Management Area '),
        ('Routing Area ', 'Routing Area '),
        ('Security Area', 'Security Area'),
        ('Transport Area', 'Transport Area'),
    )
 



    area = models.CharField(max_length=100, choices=MY_Field,default = 'choose your field')
    topic = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    about_meeting = models.TextField(max_length=500)
    zoom_url = models.URLField(max_length=200)
    time =  models.TimeField(null=True)
    date = models.DateField(null=True)
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE, default = 1)

    def __str__(self):
        return self.field
  


class StudentMeetings(models.Model):
    meetings = models.ForeignKey(Meetings,on_delete=models.CASCADE, default = 1)
    new_user = models.ForeignKey(NewUser, on_delete=models.CASCADE, default = 1)


class MeetingsRequest(models.Model):
    MY_Field = (
        ('Applications and Real-Time Area', 'Applications and Real-Time Area'),
        ('General Area', 'General Area'),
        ('Internet Area', 'Internet Area'),
        ('Operations and Management Area  ', 'Operations and Management Area '),
        ('Routing Area ', 'Routing Area '),
        ('Security Area', 'Security Area'),
        ('Transport Area', 'Transport Area'),
    )
 



    area = models.CharField(max_length=100, choices=MY_Field,default = 'choose your field')
    topic = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    about_meeting = models.TextField(max_length=500)
    zoom_url = models.URLField(max_length=200)
    time =  models.TimeField(null=True)
    date = models.DateField(null=True)
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE, default = 1)

