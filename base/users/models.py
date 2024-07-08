from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from base.users.model_managers import UserManager

# Create your models here.

class Users(AbstractBaseUser):
    user_id = models.BigAutoField(primary_key=True)
    handle = models.CharField(max_length=15, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    country_calling_code = models.CharField(max_length=5, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    password = models.CharField(max_length=128)
    role = models.ForeignKey('Roles', on_delete=models.CASCADE, db_index=True, related_name='users', null=True)
    created_at = models.DateField(auto_now_add=True)
    last_login_at = models.DateTimeField(null=True)
    initial_ip = models.CharField(max_length=40, null=True, default=True)
    last_ip = models.CharField(max_length=40, null=True, default=True)
    is_active = models.BooleanField(default=True)
    organisation = models.ForeignKey('Organizations', on_delete=models.CASCADE, db_index=True)
    
    USERNAME_FIELD = 'email'
    objects = UserManager()

class Organizations(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True, db_index=True)
    logo = models.URLField(null=True)

class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    organisation = models.ForeignKey('Organizations', on_delete=models.CASCADE)

class Permissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
class ExternalUsers(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(null=True)
    name = models.CharField(max_length=100, null=True)
    country_calling_code = models.CharField(max_length=5, null=True)
    phone_number = models.CharField(max_length=15, null=True)