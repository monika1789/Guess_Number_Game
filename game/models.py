from django.db import models

# Create your models here.
class Game(models.Model):
    secret_number = models.IntegerField()
    min_range = models.IntegerField()
    max_range = models.IntegerField()