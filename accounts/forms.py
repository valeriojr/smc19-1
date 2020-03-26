from datetime import datetime

from django import forms
from django.forms import inlineformset_factory
from django.utils import timezone

from accounts import choices
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
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']

        if password != confirm_password:
            self.add_error('confirm_password', 'As senhas não coincidem')

        return cleaned_data

