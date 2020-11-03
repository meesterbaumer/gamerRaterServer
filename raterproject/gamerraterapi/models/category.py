from django.db import models


class Category(models.Model):

    photo_link = models.CharField(max_length=5000)
    label = models.CharField(max_length=50)