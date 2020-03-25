from django.test import TestCase

from . import forms

# Create your tests here.


class AccountTests(TestCase):
    def test_blacklisted_cpf(self):
        data = {
            'cpf': '11111111111',
        }

        form = forms.AccountCreationForm(data=data)

        self.assertFalse(form.has_error('cpf'))

    def test_valid_cpf(self):
        data = {
            'cpf': '09716630417'
        }

        form = forms.AccountCreationForm(data=data)

        self.assertTrue(not form.has_error('cpf'))

    def test_invalid_cpf(self):
        data = {
            'cpf': '12345678910',
        }

        form = forms.AccountCreationForm(data=data)

        self.assertTrue(form.has_error('cpf'))

    def test_passwords_doesnt_match(self):
        data = {
            'password': '12345678',
            'confirm_password': '12345679'
        }

        form = forms.AccountCreationForm(data=data)

        self.assertFalse(form.has_error('password') or form.has_error('confirm_password'))

    def test_passwords_match(self):
        data = {
            'password': '12345678',
            'confirm_password': '12345678'
        }

        form = forms.AccountCreationForm(data=data)

        self.assertTrue(not form.has_error('password') and not form.has_error('confirm_password'))