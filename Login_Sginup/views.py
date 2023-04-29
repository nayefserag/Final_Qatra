from django.shortcuts import render, redirect
from django.contrib.auth import * 
from django.contrib import messages
from .forms import UserRegistrationForm 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.account.views import SignupView, LoginView, PasswordResetView
from django.template import RequestContext

# @login_required(login_url='login')
def home(request):
     return render(request ,'home.html')


def Sginup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')    
            return redirect('home')
    else:
        form = UserRegistrationForm()


    # return render(request, 'Sginup/Sginup.html', {'form': form})
    return render(request, 'SignUp.html', {'form': form})




def logout_view(request):
    logout(request)
    if 'form_fields' in request.session:
        del request.session['form_fields']
    return redirect('login')



def notification(request):
    return render(request,'notification.html')


def profile(request):
    return render(request,'profile.html')