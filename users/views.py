
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import NewUser


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


#def index(request):

#	return HttpResponse("hello world!")
# Create your views here.

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.

      ...
@login_required
def index(request):

    current_user = request.user
    
    if (current_user.who_is == "Admin"):
        return redirect('/admin_dashboard/')
    else:
        return redirect('/user_dashboard/')

    """

    if request.user.is_superuser:
        return redirect("/admin/")

    elif NewUser.objects.filter(id = current_user.id).exists():
        return redirect('/register/')

    else:
        
        return redirect('/login/')
    """