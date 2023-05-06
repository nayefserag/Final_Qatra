from django.shortcuts import render, redirect
from django.contrib.auth import * 
from django.contrib import messages
from .forms import UserRegistrationForm 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.account.views import SignupView, LoginView, PasswordResetView
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

@csrf_exempt
def extract_keywords(request):
    text = request.POST.get('text')
    return JsonResponse(text)

# @login_required(login_url='login')
def home(request):
     return render(request ,'Home.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             context = {'error': 'Invalid username or password' }
#             return render(request, 'login.html', context)
#     else:
#         return render(request, 'login.html')



def Sginup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=password)
                login(request, user)
                form.save()
                return redirect('home')
            except:
                form = UserRegistrationForm()
                return render(request, 'SignUp.html', {'form': form})
    else:
        form = UserRegistrationForm()

    return render(request, 'SignUp.html', {'form': form})

# def Sginup(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')    
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'SignUp.html', {'form': form})




# def logout_view(request):
#     logout(request)
#     if 'form_fields' in request.session:
#         del request.session['form_fields']
#     return redirect('login')

def logout_view(request):
    logout(request)
    if 'form_fields' in request.session:
        del request.session['form_fields']
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

# def profileedited(request):
#     profile = request.user
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile was updated successfully!')
#             return redirect('profile')
#     else:
#         form = UserRegistrationForm(instance=profile)

    
#     return render(request, 'profileedited.html', {'form': form})


# def profile_update(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            update_session_auth_hash(request, password_form.user)
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('profile_update')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserRegistrationForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)

    return render(request, 'profileedited.html', {'user_form': user_form, 'password_form': password_form})

# def profile_update(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST, instance=request.user)
#         password_form = PasswordChangeForm(user=request.user, data=request.POST)
#         if user_form.is_valid() and password_form.is_valid():
#             user_form.save()
#             update_session_auth_hash(request, password_form.user)
#             messages.success(request, 'Your profile was updated successfully!')
#             return redirect('profile_update')
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         user_form = UserRegistrationForm(instance=request.user)
#         password_form = PasswordChangeForm(user=request.user)

#     return render(request, 'profileedited.html', {'user_form': user_form, 'password_form': password_form})

# def profile_update(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')

        # Update user info
        user.username = username
        user.email = email
        if password:
            user.set_password(password)
        user.first_name = first_name
        user.save()

        messages.success(request, 'Your account information has been updated!')
        return redirect('profileeditedsuccessfully.html') # Replace with your profile page URL

    return render(request, 'profile.html')
def profile_update(request):
    # form2 = UserRegistrationForm(request.POST, instance=request.user)
    # form2 = get_object_or_404(User, pk=request.user.pk)
    user = request.user
    if request.method == 'POST':
        user = request.user
        email = request.POST.get('email')
        password = request.POST.get('password')

        if 'username' in request.POST:
            user.username = request.POST.get('username')
        if 'first_name' in request.POST:
            user.first_name = request.POST.get('first_name')

        # Update user info
        user.email = email
        if password:
            user.set_password(password)
        user.save()

        messages.success(request, 'Your account information has been updated!')
        return redirect('Profile-edited-successfully') # Replace with your profile page URL
    return render(request, 'profileedited.html',{'user': user })   

def Profile_edited_successfully(request):
    return render(request,'profileeditedsuccessfully.html')
