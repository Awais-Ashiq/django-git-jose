from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class  UserModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    text = models.TextField()

class UserModal(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_url = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)
    def __str__(self):
        return self.user.username
