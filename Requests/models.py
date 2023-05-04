# Create your models here.
from django.db import models
BLOOD_TYPES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
class BloodRequest(models.Model):
    blood_type=models.CharField(max_length=3,choices=BLOOD_TYPES,verbose_name='فصيلة الدم')
    location = models.CharField(max_length=255, verbose_name='الموقع')
    date = models.DateField(verbose_name='تاريخ اخر تبرع')

    def __str__(self):
        return f"{self.blood_type} blood requested at {self.location} on {self.date}"


class RequestDonor(models.Model):
    blood_type=models.CharField(max_length=3,choices=BLOOD_TYPES,verbose_name='فصيلة الدم')
    location = models.CharField(max_length=255, verbose_name='الموقع')
    drugs=models.CharField(max_length=255, verbose_name='الادوية اللتي يتناولها المريض')
    Patient_Status=models.CharField(max_length=255 ,verbose_name='حالة المريض')
    is_active = models.BooleanField(default=True, verbose_name='حالة الطلب')
    date = models.DateField(auto_now_add=True, verbose_name=' تاريخ عمل الطلب')

    def __str__(self):
        return f"{self.blood_type} Donor requested at {self.location} on {self.date} and it's status is{self.Patient_Status} and it's drugs is {self.drugs}"
