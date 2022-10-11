from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

class Post(models.Model):
    name = models.CharField(max_length=100) 
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)