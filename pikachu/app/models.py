from django.db import models


class Barista(models.Model):
    name = models.TextField(max_length=100)
    profile_pic = models.ImageField()


class Coffee(models.Model):
    user = models.ForeignKey(Barista, on_delete=models.CASCADE)
    date_time = models.DateTimeField('date', auto_now_add=True)
    reviews = models.TextField()
