from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MeetingsForm
from users.models import NewUser
from .models import Meetings, StudentMeetings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import MeetingSerializer, UsersSerializer

class MeetingView(viewsets.ModelViewSet):
	queryset = Meetings.objects.all()
	serializer_class = MeetingSerializer
class UsersView(viewsets.ModelViewSet):
	queryset = NewUser.objects.all()
	serializer_class = UsersSerializer

def home(request):

	return render(request,'meetings/home.html')
	#return redirect('show-all-meetings')



def about(request):

	return render(request,'meetings/about.html')


@login_required
def admin_dashboard(request):
	context = {
	        'meetings': Meetings.objects.filter(user=request.user)
	        
	    }

	return render(request,'meetings/admin_meetings.html',context)

"""
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
"""
@login_required
def admin_add_meeting(request):
	    if request.method == 'POST':
	        form = MeetingsForm(request.POST)
	        if form.is_valid():
	        	current_user = request.user
	        	instance =  form.save(commit=False)
	        	instance.user = request.user
	        	instance.save()
	        	messages.success(request, f'You have Added a new Meeting!')
	 
	        	return redirect('admin-dashboard')
	    else:
	        form = MeetingsForm()
	    return render(request,'meetings/admin_add_meeting.html',{'form': form})
#Student Part of code..

@login_required
def user_dashboard(request):
	current_user = request.user

	print(current_user.admin_key)

	data = StudentMeetings.objects.all().filter(new_user = current_user.id)

	list_of_meetings_index = []

	for meeting in data:


		list_of_meetings_index.append(meeting.meetings.id)
	context = {
	        #'meetings': Meetings.objects.all()
	        #get all record where the curent user
	        #'StudentMeetings': StudentMeetings.objects.all().filter(new_user = current_user.id)
	        #'meetings' : Meetings.objects.filter( id__in = list_of_meetings_index)
	        'meetings' : Meetings.objects.filter(user = current_user.admin_key)
	        
	    }

	
	return render(request,'meetings/user_dashboard.html',context)
@login_required
def delete_meeting(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Meetings, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return redirect('admin-dashboard')
  
    return render(request, "meetings/delete_meeting.html",context)
@login_required
def update_meeting(request,id):

    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Meetings, id = id) 
  
    # pass the object as instance in form 
    form = MeetingsForm(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return redirect('admin-dashboard')
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "meetings/update_meeting.html", context) 

def show_all_meetings(request):

	if request.method == 'POST':
		form = MeetingsFieldsForm(request.POST)
		if form.is_valid():
			area  = form.cleaned_data['area']
			request.session['area'] = area
			return HttpResponseRedirect('/meetings_by_field/')
	else:
		form = MeetingsFieldsForm()

	return render(request,'meetings/show_all_meetings.html',{'form':form})


def meeting_details(request,id):
	context = {

	  'meeting': Meetings.objects.get(id=id),

	}
	return render(request,'meetings/meeting_details.html',context)
@login_required
def save_metings_to_user_dashboard(request,id):
	current_user = request.user

	if StudentMeetings.objects.filter(meetings = Meetings.objects.get(id= id ),new_user = NewUser.objects.get(id= current_user.id )).exists():
		return redirect('user-dashboard')
		


	else:

		StudentMeetings.objects.create(
	            meetings = Meetings.objects.get(id= id ),
	            new_user = NewUser.objects.get(id= current_user.id ))


	return HttpResponseRedirect('/user_dashboard/')
@login_required
def delete_user_meeting(request, id): 
	current_user = request.user
	context ={} 
	obj = get_object_or_404(StudentMeetings, meetings = id , new_user = current_user.id ) 
	if request.method =="POST":
		obj.delete() 
		return redirect('user-dashboard')
	return render(request, "meetings/delete_user_meeting.html",context)


@login_required
def admin_area_meetings(request):
	current_user = request.user

	area_value  = current_user.area

	context = {

	  'meetings': Meetings.objects.all().filter(area = area_value),
	  'area': area_value,
	}


	return render(request,"meetings/admin_area_meetings.html",context)


