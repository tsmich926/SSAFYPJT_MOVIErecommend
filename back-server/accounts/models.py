from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    point = models.IntegerField(default=0)
    profile_path = models.TextField(null=True)
    theme= models.CharField(default="default")
    followings=models.ManyToManyField('self',symmetrical=False, related_name='followers')