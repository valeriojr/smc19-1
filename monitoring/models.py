from django.db import models

from . import choices


# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(verbose_name='Nome completo', max_length=100, blank=True, default='')
    mother_name = models.CharField(verbose_name='Nome da mãe', max_length=100, blank=True, default='')
    birth_date = models.DateField(verbose_name='Data de nascimento', null=True, blank=True)
    sus_number = models.CharField(verbose_name='Cartão do SUS', max_length=15, blank=True, null=True)
    gender = models.CharField(verbose_name='Sexo', max_length=1, choices=choices.genders, blank=True, default='')

    phone_number = models.CharField(verbose_name='Número de telefone', max_length=11, blank=True, default='')
    vaccinated = models.BooleanField(verbose_name='Tomou vacina da gripe em 2020', blank=True, default=False)
    oxygen = models.BooleanField(verbose_name='Precisou de oxigênio recentemente', blank=True, default=False)

    # Comorbidades
    diabetes = models.BooleanField(verbose_name='Diabetes', blank=True, default=False)
    heart_diseases = models.BooleanField(verbose_name='Doenças cardíacas', blank=True, default=False)
    hypertension = models.BooleanField(verbose_name='Hipertensão', blank=True, default=False)
    dementia = models.BooleanField(verbose_name='Demência', blank=True, default=False)
    bronchitis = models.BooleanField(verbose_name='Bronquite crônica', blank=True, default=False)
    cancer = models.BooleanField(verbose_name='Câncer', blank=True, default=False)
    chronic_liver_disease = models.BooleanField(verbose_name='Doença crônica no fígado', blank=True, default=False)
    chronic_kidney_disease = models.BooleanField(verbose_name='Doença renal crônica', blank=True, default=False)
    asthma = models.BooleanField(verbose_name='Asma', blank=True, default=False)
    chronic_lung_disease = models.BooleanField(verbose_name='Doença pulmonar crônica', blank=True, default=False)
    rheumatic_diseases = models.BooleanField(verbose_name='Doenças reumáticas', blank=True, default=False)
    obesity = models.BooleanField(verbose_name='Obesidade', blank=True, default=False)

    def __str__(self):
        return self.full_name


class Address(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    type = models.CharField(verbose_name='Tipo', max_length=2, choices=choices.address_types, blank=True, default='')
    postal_code = models.CharField(verbose_name='CEP', max_length=8, blank=True, default='')
    neighbourhood = models.CharField(verbose_name='Bairro', max_length=100, blank=True, default='')
    street_name = models.CharField(verbose_name='Logradouro', max_length=100, blank=True, default='')
    number = models.PositiveIntegerField(verbose_name='Número', blank=True, default=0)
    complement = models.CharField(verbose_name='Complemento', max_length=100, blank=True, default='')
    city = models.CharField(verbose_name='Cidade', max_length=100, blank=True, default='')
    people = models.PositiveIntegerField(verbose_name='Quantidade de pessoas', blank=True, default=1)

    def __str__(self):
        return '%s, %d - %s, %s, %s' % (self.street_name, self.number, self.neighbourhood, self.city, self.postal_code)


class Atendimento(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE)
    date = models.DateField(verbose_name='Data', auto_now_add=True)
    confirmed = models.BooleanField(verbose_name='Confirmado', default=False)

    def __str__(self):
        return '%s (%s)' % (self.profile, self.date.strftime('%d/%m/%Y'))


class Symptom(models.Model):
    atendimento = models.ForeignKey(Atendimento, models.CASCADE, default=1)
    symptom = models.CharField(verbose_name='Tipo de sintoma', max_length=2, choices=choices.symptoms, default='')
    intensity = models.CharField(verbose_name='Intensidade', max_length=1, choices=choices.intensities, blank=True,
                                 default='L')
    onset = models.DateField(verbose_name='Data do surgimento', blank=True, null=True)

    def __str__(self):
        return '%s %s desde %s' % (self.get_symptom_display(), self.get_intensity_display(),
                                   self.onset.strftime('%d/%m/%Y'))


class Trip(models.Model):
    profile = models.ForeignKey(Profile, models.CASCADE, default=1)
    departure_date = models.DateField(verbose_name='Ida', null=True, blank=True, default=None)
    return_date = models.DateField(verbose_name='Volta', null=True, blank=True, default=None)
    country = models.CharField(verbose_name='País', max_length=3, choices=choices.countries, default='')

    def __str__(self):
        return '%s - %s a %s' % (self.get_country_display(), self.departure_date.strftime('%d/%m/%Y'),
                                 self.return_date.strftime('%d/%m/%Y'))
