

from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [

    path('',views.home,name='home-page'),
    path('student_dashboard/',views.student_dashboard, name='student-dashboard'),
    path('professor_dashboard/',views.professor_dashboard,name="professor-dashboard"),

]
