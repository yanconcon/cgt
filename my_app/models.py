from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):

	codename=models.IntegerField(default=0)
	
	class Meta:
		db_table='MyUser'
	def__str__(self):
		return self.username