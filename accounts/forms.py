from datetime import datetime

from django import forms
from django.forms import inlineformset_factory
from django.utils import timezone
from django.forms.widgets import RadioSelect, Select
from accounts import choices
from . import models


class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = models.Account
        exclude = ['last_login', 'user_permissions', 'is_active', 'is_staff', 'is_superuser', 'groups', 'date_joined']
        widgets = {
            'password': forms.PasswordInput(),
            'user_profile': RadioSelect,
            'health_center': Select
        }
        help_texts = {
            'password': 'A senha deve ter no mínimo 8 caracteres.\nA senha não pode ser igual ao cpf.\nA senha não pode ser inteiramente númerica.\nA senha não pode ser muito comum.',
            'cpf': 'Apenas números',
            'user_profile': 'Escolha um item da lista'
        }

    confirm_password = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(AccountCreationForm, self).clean()

        #checa se todas as chaves existem
        #cleaned_data só possuem os campos válidos.
        for key in ['password', 'confirm_password', 'health_center', 'user_profile']:
            if key not in cleaned_data:
                return cleaned_data
        print(dir(self))
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        health_center = cleaned_data['health_center']
        user_profile = cleaned_data['user_profile']

        if password != confirm_password:
            self.add_error('confirm_password', 'As senhas não coincidem')
        if (user_profile == 'AU' or user_profile == 'AD') and (health_center is None):
            self.add_error('health_center', 'Você deve escolher uma unidade de saúde.')
        return cleaned_data

