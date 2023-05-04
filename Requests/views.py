from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .forms import *

def DonateRequest(request):
    if request.method == 'POST':
            form = BloodRequestForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('donate2')
    else:
        form = BloodRequestForm()
    return render(request, 'donation_reqest1.html',{'form': form})
def DonateRequestDone(request):
     return render(request, 'donation_reqest4.html')



def ReceiveRequest(request):
    if request.method == 'POST':
            form = RequestDonor(request.POST)
            if form.is_valid():
                form.save()
                return redirect('donate4')
    else:
        form = RequestDonor()
    return render(request, 'donation_reqest2.html',{'form': form})
def ReceiveRequestDone(request):
     return render(request, 'donation_reqest3.html')
