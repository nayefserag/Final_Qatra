from django.urls import path , include
from .views import *

urlpatterns = [
    path('Donate/Donation_Request/', DonateRequest ,name='donate1'),
    path('Donate/Donation_Request_Done/', DonateRequestDone,name='donate2'),
    path('Receive/Receive_Request/', ReceiveRequest,name='donate3'),
    path('Receive/Receive_Request_Done/', ReceiveRequestDone,name='donate4')

]