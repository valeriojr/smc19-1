from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class HealthCenter(models.Model):
    center_name = models.CharField(verbose_name='Nome da Unidade:', max_length=100)

    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(+90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(+180)])

    def __str__(self):
        return self.center_name

class HealthCenterStatus(models.Model):
    health_center = models.ForeignKey(HealthCenter, on_delete=models.CASCADE)
    
    date = models.DateTimeField(verbose_name='Data da atualização')
    
    beds = models.PositiveIntegerField(verbose_name='Leitos RET total', blank=False)
    occupied_beds = models.PositiveIntegerField(verbose_name='Leitos RET ocupados', blank=False)

    icus = models.PositiveIntegerField(verbose_name='Leitos UTIs total', blank=False)
    occupied_icus = models.PositiveIntegerField(verbose_name='Leitos UTIs ocupados', blank=False)

    respirators = models.PositiveIntegerField(verbose_name='Respiradores total', blank=False)
    occupied_respirators = models.PositiveIntegerField(verbose_name='Respiradores ocupados', blank=False)

    necessary_beds = models.PositiveIntegerField(verbose_name='Leitos RET necessários', blank=False)
    necessary_icus = models.PositiveIntegerField(verbose_name='Leitos UTIs necessários', blank=False)
    necessary_respirators = models.PositiveIntegerField(verbose_name='Respiradores necessários', blank=False)

    def __str__(self):
        return 'Status da unidade ' + str(self.health_center.center_name) + ' em ' + str(self.date) 