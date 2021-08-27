from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MeetingsForm, MeetingsFieldsForm
from users.models import NewUser
from .models import Meetings, StudentMeetings
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
def professor_add_meeting(request):
	    if request.method == 'POST':
	        form = MeetingsForm(request.POST)
	        if form.is_valid():
	        	current_user = request.user
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
	current_user = request.user

	data = StudentMeetings.objects.all().filter(new_user = current_user.id)

	list_of_meetings_index = []

	for meeting in data:


		list_of_meetings_index.append(meeting.meetings.id)
	context = {
	        #'meetings': Meetings.objects.all()
	        #get all record where the curent user
	        #'StudentMeetings': StudentMeetings.objects.all().filter(new_user = current_user.id)
	        'meetings' : Meetings.objects.filter( id__in = list_of_meetings_index)
	        
	    }

	
	return render(request,'meetings/student_dashboard.html',context)

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
        return redirect('professor-dashboard')
  
    return render(request, "meetings/delete_meeting.html",context)

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
        return redirect('professor-dashboard')
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "meetings/update_meeting.html", context) 

def show_all_meetings(request):

	if request.method == 'POST':
		form = MeetingsFieldsForm(request.POST)
		if form.is_valid():
			field  = form.cleaned_data['field']
			request.session['field'] = field
			return HttpResponseRedirect('/meetings_by_field/')
	else:
		form = MeetingsFieldsForm()

	return render(request,'meetings/show_all_meetings.html',{'form':form})

def meetings_by_field(request):
	field_value  = request.session['field']

	context = {

	  'meetings': Meetings.objects.all().filter(field = field_value),
	  'field': field_value,
	}
	return render(request,'meetings/meetings_by_field.html',context)

def save_metings_to_student_dashboard(request,id):
	current_user = request.user

	StudentMeetings.objects.create(
            meetings = Meetings.objects.get(id= id ),
            new_user = NewUser.objects.get(id= current_user.id )
    )

	messages.success(request, f'Your meeting has been added!')

	return HttpResponseRedirect('/student_dashboard/')