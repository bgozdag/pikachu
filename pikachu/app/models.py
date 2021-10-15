from django.db import models


class Barista(models.Model):
    name = models.TextField(max_length=100)
    profile_pic = models.ImageField(default='pp-default.png')
    mail = models.TextField(default='', max_length=100)

    def __str__(self):
        return self.name


class Coffee(models.Model):
    user = models.ForeignKey(Barista, on_delete=models.CASCADE)
    date_time = models.DateTimeField('date', auto_now_add=True)
    reviews = models.TextField()
