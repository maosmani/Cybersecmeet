

from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [


    path('',views.home,name='home-page'),
    path('about/',views.about,name='about-page'),
    path('student_dashboard/',views.student_dashboard, name='student-dashboard'),
    path('professor_dashboard/',views.professor_dashboard,name="professor-dashboard"),
    #path('professor_meetings/',views.professor_meetings,name="professor-meetings"),
    path('professor_add_meeting/',views.professor_add_meeting,name="professor-add-meeting"),

]
