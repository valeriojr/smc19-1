from django.db import models
from django.contrib.auth.models import AbstractUser

from . import choices

# Create your models here.


class Profile(AbstractUser):
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=choices.genders)
    phone_number = models.CharField(max_length=11)

    REQUIRED_FIELDS = ['cpf', 'birth_date', 'gender', 'phone_number', 'first_name', 'last_name', 'password1', 'password2']

    def __str__(self):
        return self.get_full_name()


class Address(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    type = models.CharField(max_length=2, choices=choices.address_types)
    postal_code = models.CharField(max_length=8)
    neighbourhood = models.CharField(max_length=2, choices=choices.neighbourhoods)
    street_name = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    complement = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=3, choices=choices.cities)
    people = models.PositiveIntegerField()


class Trip(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    departure_date = models.DateField()
    return_date = models.DateField()
    country = models.CharField(max_length=3, choices=choices.countries)


class Symptom(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    symptom = models.CharField(max_length=2, choices=choices.symptoms)
    intensity = models.CharField(max_length=1, choices=choices.intensities)
    onset = models.DateField()


class Comorbidity(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    type = models.CharField(max_length=1, choices=choices.comorbidities)
