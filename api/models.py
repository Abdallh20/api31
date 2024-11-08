from django.db import models
from datetime import datetime
# Create your models here.
#guest --- hall ---reservation

class location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    images = models.TextField(max_length=1000000000000000000000000,default="")
    is_accident = models.BooleanField()
    is_fire = models.BooleanField()

    def __str__(self):
        return f"({self.longitude}, {self.latitude})"
