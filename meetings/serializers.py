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
		fields = ('id','who_is','admin_key')
		#'email','user_name',