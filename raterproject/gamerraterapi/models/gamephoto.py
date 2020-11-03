from django.db import models
from django.contrib.auth.models import User

class GamePhoto(models.Model):

    photo_link = models.CharField(max_length=5000)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)