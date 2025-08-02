from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    photo = models.ImageField(upload_to='tweets/', blank=True, null=True)