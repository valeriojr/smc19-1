from django.test import TestCase
from django.utils import timezone

from . import forms


# Create your tests here.


class SymptomCreateFormTests(TestCase):
    def test_future_onset(self):
        form = forms.SymptomCreateForm(data={
            'type': 'TR',
            'intensity': 'L',
            'onset': timezone.now() + timezone.timedelta(days=1),
        })

        self.assertFalse(form.is_valid())


class TripCreateFormTests(TestCase):
    def test_departure_after_return(self):
        form = forms.TripForm(data={
            'departure_date': '01/01/1970',
            'return_date': '31/12/1969',
            'country': 'BRA'
        })

        self.assertFalse(form.is_valid())