from django import forms
from django.forms import inlineformset_factory

from . import models


class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = models.Account
        exclude = ['last_login', 'user_permissions', 'is_active', 'is_staff', 'is_superuser', 'groups', 'date_joined']
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'password': 'Inserir critérios de validação',
            'cpf': 'Apenas números'
        }

    confirm_password = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(AccountCreationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'As senhas não coincidem')

        return cleaned_data


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        exclude = ['account']
        widgets = {
            'birth_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }


AddressFormset = inlineformset_factory(models.Profile, models.Address, fields='__all__', extra=1, can_delete=True,
                                       widgets={
                                           'postal_code': forms.TextInput(attrs={'class': 'postal-code-field'}),
                                           'complement': forms.Textarea(attrs={'rows': 2}),
                                       })
