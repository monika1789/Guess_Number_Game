from django.db import models

# Create your models here.
class Game(models.Model):
    secret_number = models.IntegerField()
    min_range = models.IntegerField(default=1)
    max_range = models.IntegerField(default=10)