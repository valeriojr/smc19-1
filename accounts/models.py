from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models here.
import validators


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
    cpf = models.CharField(verbose_name='CPF', max_length=11, unique=True, validators=[validators.validate_cpf])

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
