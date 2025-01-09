
from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    condition = models.CharField(max_length=100)
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temperature}°C"


