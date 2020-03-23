from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

from . import choices


# Create your models here.


class Profile(AbstractUser):
    username = None
    first_name = None
    last_name = None
    cpf = models.CharField(verbose_name='CPF', max_length=11, unique=True)
    full_name = models.CharField(verbose_name='Nome completo', max_length=100, blank=True, default='')
    mother_name = models.CharField(verbose_name='Nome da mãe', max_length=100, blank=True, default='')
    birth_date = models.DateField(verbose_name='Data de nascimento', null=True, blank=True)
    gender = models.CharField(verbose_name='Sexo', max_length=1, choices=choices.genders, blank=True, default='')
    phone_number = models.CharField(verbose_name='Número de telefone', max_length=11, blank=True, default='')

    REQUIRED_FIELDS = ['password1', 'password2']
    USERNAME_FIELD = 'cpf'

    def __str__(self):
        return self.full_name


class Address(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    type = models.CharField(verbose_name='Tipo', max_length=2, choices=choices.address_types, blank=True, default='')
    postal_code = models.CharField(verbose_name='CEP', max_length=8, blank=True, default='')
    neighbourhood = models.CharField(verbose_name='Bairro', max_length=2, choices=choices.neighbourhoods, blank=True, default='')
    street_name = models.CharField(verbose_name='Logradouro', max_length=100, blank=True, default='')
    number = models.PositiveIntegerField(verbose_name='Número', blank=True, default=0)
    complement = models.CharField(verbose_name='Complemento', max_length=100, blank=True, default='')
    city = models.CharField(verbose_name='Cidade', max_length=3, choices=choices.cities, blank=True, default='')
    people = models.PositiveIntegerField(verbose_name='Quantidade de pessoas', blank=True, default=1)


class Trip(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    departure_date = models.DateField(verbose_name='Ida', null=True, blank=True, default=None)
    return_date = models.DateField(verbose_name='Volta', null=True, blank=True, default=None)
    country = models.CharField(verbose_name='País', max_length=3, choices=choices.countries, blank=True, default='')


class Symptom(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    symptom = models.CharField(verbose_name='Tipo de sintoma', max_length=2, choices=choices.symptoms, default='')
    intensity = models.CharField(verbose_name='Intensidade', max_length=1, choices=choices.intensities, default='')
    onset = models.DateField(verbose_name='Data do surgimento', blank=True, null=True)


class Comorbidity(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    type = models.CharField(verbose_name='Tipo', max_length=1, choices=choices.comorbidities, blank=True)
