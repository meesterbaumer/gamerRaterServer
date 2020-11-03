from django.db import models
from django.contrib.auth.models import User

class GameRating(models.Model):

    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)