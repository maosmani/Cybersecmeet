from django import forms 
from users.models import NewUser
from django.forms import ModelForm
from .models import Meetings
from django.utils.safestring import mark_safe


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
    input_formats = '%H:%M:%S %Z'

    #'time': forms.TimeInput(format='%H:%M'),
"""
class MeetingsForm(forms.Form):
    MY_Field = (
        ('electronic', 'electronic'),
        ('computer', 'computer'),
        ('economic', 'economic'),
        )
    field = models.CharField(max_length=100, choices=MY_Field,default = 'choose your field')
    topic = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    about_meeting = models.TextField()
    zoom_url = models.URLField(max_length=200)
    time =  models.TimeField(null=True)
    date = models.DateField(null=True)
"""
class MeetingsForm(ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = Meetings
        fields = ['topic','title','zoom_url','zoom_password','about_meeting','date','time']
        widgets = {
            'date': DateInput(),
            'time':TimeInput(),


            }
      


