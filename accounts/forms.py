from django import forms
from django.forms import inlineformset_factory

from . import models


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['first_name', 'last_name', 'username', 'password', 'cpf', 'birth_date', 'gender']


AddressFormset = inlineformset_factory(models.Profile, models.Address, fields='__all__', extra=1, can_delete=False)
