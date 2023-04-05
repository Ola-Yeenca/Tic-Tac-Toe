from django.db import models

# Create your models here.
class Game(models.Model):
    state = models.CharField(max_length=9)
    turn = models.CharField(max_length=1)
    # winner = models.CharField(max_length=1, blank=True)
