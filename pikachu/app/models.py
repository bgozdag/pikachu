from django.db import models


class User(models.Model):
    name = models.TextField()
    profile_pic = models.ImageField()


class Coffee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField('date', auto_now_add=True)
    reviews = models.TextField()
