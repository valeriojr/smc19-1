from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

class HealthCenter(models.Model):
    center_name = models.CharField(verbose_name='Nome da Unidade:', max_length=100)
    
    beds = models.PositiveIntegerField(verbose_name='Leitos total', default=0)
    occupied_beds = models.PositiveIntegerField(verbose_name='Leitos ocupados', default=0)
    
    icus = models.PositiveIntegerField(verbose_name='UTIs total', default=0)
    occupied_icus = models.PositiveIntegerField(verbose_name='UTIs ocupadas', default=0)
    
    respirators = models.PositiveIntegerField(verbose_name='Respiradores total', default=0)
    occupied_respirators = models.PositiveIntegerField(verbose_name='Respiradores ocupados', default=0)

    necessary_beds = models.PositiveIntegerField(verbose_name='Leitos necessários', default=0)
    necessary_icus = models.PositiveIntegerField(verbose_name='UTIs necessárias', default=0)
    necessary_respirators = models.PositiveIntegerField(verbose_name='UTIs necessárias', default=0)

    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(+90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(+180)])

    def __str__(self):
        return self.center_name 