from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import MeetingsForm
from users.models import NewUser
from .models import Meetings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

def home(request):

	return render(request,'meetings/home.html')



def about(request):

	return render(request,'meetings/about.html')


#Prof part of the code
"""
@login_required
def professor_dashboard(request):
	

	    return render(request,'meetings/professor_dashboard.html')

"""
@login_required
def professor_dashboard(request):
	context = {
	        'meetings': Meetings.objects.filter(user=request.user)
	        
	    }

	return render(request,'meetings/professor_meetings.html',context)


@login_required
def professor_add_meeting(request):
	    if request.method == 'POST':
	        form = MeetingsForm(request.POST)
	        if form.is_valid():
	        	current_user = request.user
	        	print(current_user.id)
	        	instance =  form.save(commit=False)
	        	instance.user = request.user
	        	instance.save()
	        	messages.success(request, f'You have Added a new Meeting!')
	 
	        	return redirect('professor-dashboard')
	    else:
	        form = MeetingsForm()
	    return render(request,'meetings/professor_add_meeting.html',{'form': form})


#Student Part of code..

@login_required
def student_dashboard(request):
	context = {
	        'meetings': Meetings.objects.all()
	        
	    }

	
	return render(request,'meetings/student_dashboard.html',context)
