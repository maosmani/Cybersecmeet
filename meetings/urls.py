
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('admin_keys', views.UsersView)



urlpatterns = [

    path('',views.home,name='home-page'),
    path('chooseadmins/',include(router.urls)),
    path('home/',views.show_all_meetings, name="show-all-meetings"),
    path('about/',views.about,name='about-page'),
    path('request_meeting', views.request_meeting, name="request-meeting" ),
    path('show_meetings_request', views.show_meetings_request, name="show-meetings-request" ),
    path('user_dashboard/',views.user_dashboard, name='user-dashboard'),
    path('admin_dashboard/',views.admin_dashboard,name="admin-dashboard"),
    path('admin_area_meetings/',views.admin_area_meetings,name="admin-area-meetings"),
    #path('professor_meetings/',views.professor_meetings,name="professor-meetings"),
    path('admin_add_meeting/',views.admin_add_meeting,name="admin-add-meeting"),
    path('delete/<int:id>/', views.delete_meeting, name="deletes" ),
    path('update/<int:id>/',views.update_meeting, name="update"),
    #path('meetings/',views.show_all_meetings, name="show-all-meetings"),
    path('meetings_by_field/',views.meetings_by_field, name="meetings-by-field"),
    path('meeting_details/<int:id>/',views.meeting_details,name="meeting-details"),
    path('meeting_save_to_user/<int:id>>/',views.save_metings_to_user_dashboard,name="save-meeting-to-user-dashoard"),
    path('delete_user_meeting/<int:id>/', views.delete_user_meeting, name="delete-user-meeting" ),
    path('delete_requested_meeting/<int:id>/', views.delete_requested_meeting, name="delete-requested-meeting" ),
    path('accept_requested_meeting/<int:id>/', views.accept_requested_meeting, name="accept-reqested-meeting" ),


]
