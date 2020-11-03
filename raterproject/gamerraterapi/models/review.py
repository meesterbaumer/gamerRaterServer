from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):

    body = models.CharField(max_length=500)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)