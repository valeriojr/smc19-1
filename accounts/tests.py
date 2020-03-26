from django.test import TestCase
from django.utils import timezone

from . import forms

# Create your tests here.


class AccountTests(TestCase):
    def test_blacklisted_cpf(self):
        data = {
            'cpf': '11111111111',
            'password': '12345678',
            'confirm_password': '12345678'
        }

        form = forms.AccountCreationForm(data=data)

        self.assertTrue(form.has_error('cpf'))

    def test_valid_cpf(self):
        data = {
            'cpf': '09716630417',
            'password': '12345678',
            'confirm_password': '12345678'
        }

        form = forms.AccountCreationForm(data=data)

        self.assertTrue(not form.has_error('cpf'))

    def test_invalid_cpf(self):
        data = {
            'cpf': '12345678910',
            'password': '12345678',
            'confirm_password': '12345678'
        }

        form = forms.AccountCreationForm(data=data)

        self.assertTrue(form.has_error('cpf'))

    def test_passwords_doesnt_match(self):
        data = {
            'cpf': '09716630417',
            'password': '12345678',
            'confirm_password': '12345679'
        }

        form = forms.AccountCreationForm(data=data)

        self.assertTrue(form.has_error('confirm_password'))

    def test_passwords_match(self):
        data = {
            'cpf': '09716630417',
            'password': '12345678',
            'confirm_password': '12345678'
        }

        form = forms.AccountCreationForm(data=data)

        self.assertTrue(not form.has_error('password') and not form.has_error('confirm_password'))
