from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flight(models.Model):
    fromm=models.CharField(max_length=30)
    to=models.CharField(max_length=30)
    datee=models.CharField(max_length=30)
    paym=models.CharField(max_length=6)
    def __str__(self):
        return str(self.fromm)


class Feedback(models.Model):
    email=models.EmailField()
    username=models.CharField(max_length=50)
    address=models.TextField()
    gender=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return str(self.email)

class Profile (models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about=models.CharField(max_length=200,blank=True)


    def __str__(self):
        return str(self.user)