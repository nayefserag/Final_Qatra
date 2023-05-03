from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import * 
from django.contrib import messages
from .forms import UserRegistrationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
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
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'SignUp.html', {'form': form})




# def logout_view(request):
#     logout(request)
#     if 'form_fields' in request.session:
#         del request.session['form_fields']
#     return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

def notification(request):
    return render(request,'notification.html')


def profile(request):
    form = UserRegistrationForm (instance=request.user)
    return render(request,'profile.html',{'form': form})



# def profileedited(request):
#         if request.method == 'POST':
#          form = UserRegistrationForm(request.POST, instance=request.user)
#             if form.is_valid():
#              form.save()
#             messages.success(request, 'Your profile was successfully updated!')
#             return redirect('profile')
#         else:
#             form = UserRegistrationForm(instance=request.user)
#         return render(request, 'profileedited', {'form': form})

# def profileedited(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile was successfully updated!')
#             return redirect('profile22')
#     else:
#         form = UserRegistrationForm(instance=request.user)
#     return render(request, 'profileedited.html', {'form': form})



# def profileedited(request):
#     form = UserRegistrationForm(request.POST if request.POST else None)
#     if request.method == 'POST':
#      if form.is_valid():
#         form.save()     
#         return redirect('profile')  

#     return render(request, 'profileedited.html', {'form': form})




#########
# في هنا خرا خرا خرا
##########

def profileedited(request):
    profile = request.user
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('profile')
    else:
        form = UserRegistrationForm(instance=profile)

    
    return render(request, 'profileedited.html', {'form': form})
