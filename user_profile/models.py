from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser


class User(AbstractBaseUser,PermissionsMixin):
    
   """

   Custom user class.
   
   """ 
   username = models.CharField('username', max_length=10,unique=True, db_index=True)
   email = models.EmailField('email address', unique=True)
   joined = models.DateTimeField(auto_now_add=True)
   is_active = models.BooleanField(default=True)
   is_admin = models.BooleanField(default=False)
   is_staff= models.BooleanField(default=True)
   is_superuser=models.BooleanField(default=False)
   
   USERNAME_FIELD = 'username'
   
   
   def __unicode__(self):
       return self.username