from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from . import choices


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, cpf, password=None):
        user = self.model(cpf=cpf)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, cpf, password=None):
        user = self.create_user(cpf=cpf, password=password)

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class Account(AbstractUser):
    username = None
    first_name = None
    last_name = None
    cpf = models.CharField(verbose_name='CPF', max_length=11, unique=True)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


class Profile(models.Model):


    full_name = models.CharField(verbose_name='Nome completo', max_length=100, blank=True, default='')
    mother_name = models.CharField(verbose_name='Nome da mãe', max_length=100, blank=True, default='')
    birth_date = models.DateField(verbose_name='Data de nascimento', null=True, blank=True)
    sus_number = models.CharField(verbose_name='Cartão do SUS', max_length=15, blank=True, null=True)
    gender = models.CharField(verbose_name='Sexo', max_length=1, choices=choices.genders, blank=True, default='')
    phone_number = models.CharField(verbose_name='Número de telefone', max_length=11, blank=True, default='')
    vaccinated = models.BooleanField(verbose_name='Vacinado', blank=True, default=False)

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
