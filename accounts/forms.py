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

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']

        # verificar o tamanho da string
        if len(cpf) != 11:
            self.add_error('cpf', 'O CPF deve conter exatamente 11 dígitos')
            return cpf

        # cpfs inválidos
        for i in range(10):
            if cpf == str(i) * 11:
                self.add_error('cpf', 'CPF inválido')
                return cpf

        # validação do primeiro dígito verificador
        s = 0
        for i in range(9):
            s += int(cpf[i]) * (10 - i)
        first_digit_valid = int(cpf[9]) == ((s * 10 % 11) % 10)

        # validação do segundo dígito verificador
        s = 0
        for i in range(10):
            s += int(cpf[i]) * (11 - i)
        second_digit_valid = int(cpf[10]) == ((s * 10 % 11) % 10)

        if first_digit_valid and second_digit_valid:
            return cpf

        self.add_error('cpf', 'CPF inválido')
        return cpf

    def clean(self):
        cleaned_data = super(AccountCreationForm, self).clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']

        if password != confirm_password:
            self.add_error('confirm_password', 'As senhas não coincidem')

        return cleaned_data

