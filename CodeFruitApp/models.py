from django.db import models
class User(models.Model):

    UserName = models.CharField(max_length=20)
    UserPass = models.CharField(max_length=20)