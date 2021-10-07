from rest_framework import serializers
from .models import Meetings
from users.models import NewUser


class MeetingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meetings
		fields = ('title','time')


class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewUser
		fields = ('id','email','user_name','who_is','admin_key')