from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models


# class UserManager(BaseUserManager):
#     def create_user(self, email, phone, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         if not phone:
#             raise ValueError('The Phone field must be set')

#         email = self.normalize_email(email)
#         user = self.model(email=email, phone=phone, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, phone, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, phone, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15, unique=True)
#     username = models.CharField(max_length=30, unique=True, null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['phone']

#     objects = UserManager()

#     def __str__(self):
#         return self.email




