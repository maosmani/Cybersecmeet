from django import forms 
from users.models import NewUser
from django.forms import ModelForm
from .models import Meetings, MeetingsRequest
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
        fields = ['topic','title','zoom_url','about_meeting','date','time']
        widgets = {
            'date': DateInput(),
            'time':TimeInput(),


            }
      



class MeetingsFieldsForm(forms.Form):
    OPTIONS = (
        ('Applications and Real-Time Area', 'Applications and Real-Time Area'),
        ('General Area', 'General Area'),
        ('Internet Area', 'Internet Area'),
        ('Operations and Management Area  ', 'Operations and Management Area '),
        ('Routing Area ', 'Routing Area '),
        ('Security Area', 'Security Area'),
        ('Transport Area', 'Transport Area'),
    )
    area = forms.ChoiceField(choices = OPTIONS)



class RequestMeetingForm(ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = MeetingsRequest
        fields = ['area','topic','title','zoom_url','about_meeting','date','time']
        widgets = {
            'date': DateInput(),
            'time':TimeInput(),


            }
      

