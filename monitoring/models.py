from django.db import models

from accounts.models import Profile
from . import choices


# Create your models here.


class Atendimento(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    date = models.DateField(verbose_name='Data', auto_now_add=True)
    confirmed = models.BooleanField(verbose_name='Confirmado', default=False)


class Trip(models.Model):
    atendimento = models.ForeignKey(Atendimento, models.CASCADE, default=1)
    departure_date = models.DateField(verbose_name='Ida', null=True, blank=True, default=None)
    return_date = models.DateField(verbose_name='Volta', null=True, blank=True, default=None)
    country = models.CharField(verbose_name='País', max_length=3, choices=choices.countries, blank=True, default='')


class Symptom(models.Model):
    atendimento = models.ForeignKey(Atendimento, models.CASCADE, default=1)
    symptom = models.CharField(verbose_name='Tipo de sintoma', max_length=2, choices=choices.symptoms, default='')
    intensity = models.CharField(verbose_name='Intensidade', max_length=1, choices=choices.intensities, default='')
    onset = models.DateField(verbose_name='Data do surgimento', blank=True, null=True)


class Comorbidity(models.Model):
    atendimento = models.ForeignKey(Atendimento, models.CASCADE, default=1)
    type = models.CharField(verbose_name='Tipo', max_length=1, choices=choices.comorbidities, blank=True)
