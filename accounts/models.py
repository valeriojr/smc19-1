from django.db import models
from django.contrib.auth.models import AbstractUser

from . import choices

# Create your models here.


class Profile(AbstractUser):
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    birth_date = models.DateField(verbose_name='Data de nascimento')
    gender = models.CharField(verbose_name='Sexo', max_length=1, choices=choices.genders)
    phone_number = models.CharField(verbose_name='Número de telefone', max_length=11)

    REQUIRED_FIELDS = ['cpf', 'birth_date', 'gender', 'phone_number', 'first_name', 'last_name', 'password1', 'password2']

    def __str__(self):
        return self.get_full_name()


class Address(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    type = models.CharField(verbose_name='Tipo', max_length=2, choices=choices.address_types)
    postal_code = models.CharField(verbose_name='CEP', max_length=8)
    neighbourhood = models.CharField(verbose_name='Bairro', max_length=2, choices=choices.neighbourhoods)
    street_name = models.CharField(verbose_name='Logradouro', max_length=100)
    number = models.PositiveIntegerField(verbose_name='Número')
    complement = models.CharField(verbose_name='Complemento', max_length=100, blank=True)
    city = models.CharField(verbose_name='Cidade', max_length=3, choices=choices.cities)
    people = models.PositiveIntegerField(verbose_name='Quantidade de pessoas')


class Trip(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    departure_date = models.DateField(verbose_name='Ida')
    return_date = models.DateField(verbose_name='Volta')
    country = models.CharField(verbose_name='País', max_length=3, choices=choices.countries)


class Symptom(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    symptom = models.CharField(verbose_name='Tipo de sintoma', max_length=2, choices=choices.symptoms)
    intensity = models.CharField(verbose_name='Intensidade', max_length=1, choices=choices.intensities)
    onset = models.DateField(verbose_name='Data do surgimento')


class Comorbidity(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    type = models.CharField(verbose_name='Tipo', max_length=1, choices=choices.comorbidities)
