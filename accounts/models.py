from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django_countries.fields import CountryField
from django.core.mail import send_mail
# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, user_name, password, **other_fields)
    
    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError(('you must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email = email, user_name=user_name, **other_fields) 
        user.set_password(password)
        user.save()
        return user
 


class UserBase(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique = True)
    first_name = models.CharField(max_length=150, blank= True)
    last_name = models.CharField(max_length=150, blank= True)
    country = CountryField()
    created = models.DateTimeField(auto_now_add=True)
    updated  =  models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS  = ['user_name']


    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta: 
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"
    def __str__(self):
        return self.user_name
    
    