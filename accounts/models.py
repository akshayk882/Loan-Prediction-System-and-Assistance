from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):


    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    # portfolio_site = models.URLField(blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

def __str__(self):
  return self.user.username


