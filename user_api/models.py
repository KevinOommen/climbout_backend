from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class AppUserManager(BaseUserManager):
	def create_user(self, username , password=None):
		if not username:
			raise ValueError('A username is required.')
		if not password:
			raise ValueError('A password is required.')
		
		user = self.model(email=username)
		user.set_password(password)
		user.save()
		return user
	
	def create_superuser(self, username, password=None):
		if not username:
			raise ValueError('A username is required.')
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(username, password)
		user.is_superuser = True
		user.save()
		return user


class AppUser(AbstractBaseUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=50)
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []
	objects = AppUserManager()
	def __str__(self):
		return self.username