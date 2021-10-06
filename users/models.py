from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django_countries.fields import CountryField

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    MY_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    
    )
    MY_Field = (
        ('Applications and Real-Time Area', 'Applications and Real-Time Area'),
        ('General Area', 'General Area'),
        ('Internet Area', 'Internet Area'),
        ('Operations and Management Area  ', 'Operations and Management Area '),
        ('Routing Area ', 'Routing Area '),
        ('Security Area', 'Security Area'),
        ('Transport Area', 'Transport Area'),
    
    )

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    who_is = models.CharField(max_length= 100 ,choices=MY_CHOICES,default = 'User')
    area = models.CharField(max_length=100, choices=MY_Field,default = 'electronic')
    country = CountryField()
    about = models.TextField(blank=True)
    zoom_url = models.URLField(max_length = 200 , default = "")
    admin_key = models.CharField(max_length=150, blank=True)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name
   