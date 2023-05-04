from django import forms
from .models import *


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['blood_type', 'location', 'date']
        labels = {
            'blood_type'  :'فصيلة الدم ',
            'location' : 'الموقع ',
            'date' : 'تاريخ اخر تبرع',

        } 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.Meta.labels.items():
            self[k].label = v




class RequestDonor(forms.ModelForm):
    class Meta:
        model = RequestDonor
        fields = ['blood_type', 'location', 'drugs','Patient_Status']
        labels = {
            'blood_type'  :'فصيلة الدم ',
            'location' : 'الموقع ',
            'drugs' : 'الأدوية التي يتناولها المريض',
            'Patient_Status':'حالة المريض',
        } 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.Meta.labels.items():
            self[k].label = v


