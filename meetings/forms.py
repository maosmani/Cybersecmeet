from django import forms 
from users.models import NewUser
from django.forms import ModelForm
from .models import Meetings

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
    input_formats = ' %h:%m %p'

    #'time': forms.TimeInput(format='%H:%M'),
 
class MeetingsForm(ModelForm):
    #email = forms.EmailField()

    class Meta:
        model = Meetings
        fields = ['topic','title','zoom_url','about_meeting','date','time']
        widgets = {
            'date': DateInput(),
            'time':TimeInput(),
            }