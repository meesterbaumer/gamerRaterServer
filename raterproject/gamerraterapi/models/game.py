from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    year_released = models.CharField(max_length=50)
    num_players = models.IntegerField()
    length_play = models.CharField(max_length=50)
    age_rec = models.CharField(max_length=50)
    designer = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)