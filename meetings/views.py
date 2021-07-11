from django.shortcuts import render
from django.http import HttpResponse

def home(request):

	return render(request,'meetings/home.html')
# Create your views here.

def student_dashboard(request):
	
	return render(request,'meetings/student_dashboard.html')

def professor_dashboard(request):

	return render(request,'meetings/professor_dashboard.html')