from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.core.validators import RegexValidator   
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import *



CHOICES1 = (('ذكر','ذكر'),
            ('انثى','انثى'))
CHOICES2 = (('A+','A+'),
            ('O+','O+'),
            ('B+','B+'),
            ('AB+','AB+'),
            ('A-','A-'),
            ('O-','O'),
            ('A-','A-'),
            ('B-','B-'),
            ('AB-','AB-'))
CHOICES3 = (('نعم','نعم'),
            ('لا','لا'))
class UserRegistrationForm(UserCreationForm):

    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone = forms.CharField(max_length=20,validators=[phone_regex],label='رقم الهاتف :')

    # age = forms.IntegerField( required=True,label='العمر')
    # identity = forms.CharField(max_length=101,label='رقم الهويه')
    # gender = forms.ChoiceField(choices=CHOICES1, required=True,label='النوع')
    # blood_type=forms.ChoiceField(choices=CHOICES2,label='فصيلة الدم')
    # The_last_donate=forms.CharField(initial=timezone.now,label='تاريخ اخر تبرع')
    # issuse=forms.ChoiceField(choices=CHOICES3,label='هل تعاني من أي امراض مزمنه؟')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2', )

        labels = {
            'username'  :'الاسم بالكامل',
            'password1' : 'كلمة المرور',
            'password2' : 'تأكيد كلمة المرور',
            'email':'البريد الالكتروني', 
            'first_name':'رقم الهاتف'
        } 

        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.Meta.labels.items():
            self[k].label = v
class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), strip=False, help_text='Something Is wrong ')
    new_password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), strip=False)

    class Meta:
        model = User
        fields ='__all__'