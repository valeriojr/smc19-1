from datetime import datetime

from django import forms
from django.forms import inlineformset_factory
from django.utils import timezone
from django.forms.widgets import RadioSelect
from accounts import choices
from . import models


class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = models.Account
        exclude = ['last_login', 'user_permissions', 'is_active', 'is_staff', 'is_superuser', 'groups', 'date_joined']
        widgets = {
            'password': forms.PasswordInput(),
            'user_profile': RadioSelect,
            'health_center': RadioSelect
        }
        help_texts = {
            'password': 'Inserir critérios de validação',
            'cpf': 'Apenas números',
            'user_profile': 'Escolha um item da lista'
        }

    confirm_password = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(AccountCreationForm, self).clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        user_profile = cleaned_data['user_profile']

        if password != confirm_password:
            self.add_error('confirm_password', 'As senhas não coincidem')

        return cleaned_data

