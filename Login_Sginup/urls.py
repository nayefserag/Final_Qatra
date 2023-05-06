from .views import * 
from django.urls import path ,include 
from django.contrib.auth import views
from django.views.generic import TemplateView


from django.contrib.auth.views import (
    LogoutView, 
    LoginView,
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('', home , name = 'home'),
    path('accounts/', include('allauth.urls') ,name='accounts'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('logout/',logout_view,name= 'logout'),
    path('notification/',notification , name= 'notification'),
    path('login/',views.LoginView.as_view(template_name='login.html'), name='login'),
    path('SignUp/',Sginup, name='SignUp'),
    path('yourprofile/',profile,name='profile'),
    path('Edit_Your_Profile/',profile_update , name='profile_edit'),
    path('Profile-edited-successfully/',Profile_edited_successfully , name='Profile-edited-successfully'),
    path('logout/', views.LogoutView.as_view(template_name='Sginin/logout.html'), name='logout'),
    path('password-reset/',views.PasswordResetView.as_view(template_name='forget_password_1.html'), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name='forget_password_2.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='forget_password_3.html'), name='password_reset_confirm'),
    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(template_name='forget_password_4.html'), name='password_reset_complete'),

    ##

  #  path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
  #  path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name='Reset/password_reset_done.html'), name='password_reset_done'),
   # path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
  #  path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   # path('password-reset-complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]   



