from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

class HealthCenter(models.Model):
    center_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(+90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(+180)]) 