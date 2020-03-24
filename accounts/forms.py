from django import forms
from django.forms import inlineformset_factory

from . import models


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        exclude = ['last_login', 'user_permissions', 'is_active', 'is_staff', 'is_superuser', 'groups', 'date_joined']
        widgets = {
            'password': forms.PasswordInput(),
            'birth_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
        }

    field_order = ['cpf', 'password', 'full_name', 'mother_name', 'sus_number']


AddressFormset = inlineformset_factory(models.Profile, models.Address, fields='__all__', extra=1, can_delete=True)
