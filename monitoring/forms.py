from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory, CheckboxSelectMultiple
from django.utils.datetime_safe import datetime
from django.utils.timezone import now

from . import models


class AtendimentoCreateForm(forms.ModelForm):
    class Meta:
        model = models.Atendimento
        fields = '__all__'
        labels = {
            'profile': 'Paciente'
        }


class SymptomCreateForm(forms.ModelForm):
    class Meta:
        model = models.Symptom
        fields = '__all__'
        widgets = {
            'symptom': CheckboxSelectMultiple,
            'onset': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
        }

    def clean_onset(self):
        onset = self.cleaned_data['onset']

        if onset > now().date():
            self.add_error('onset', 'Surgimento de sintoma(s) no futuro')

        return onset


class TripCreateForm(forms.ModelForm):
    class Meta:
        model = models.Trip
        fields = '__all__'
        widgets = {
            'departure_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'return_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'country': CheckboxSelectMultiple
        }

    def clean_departure_date(self):
        departure_date = self.cleaned_data['departure_date']

        if departure_date > now().date():
            self.add_error('departure_date', 'Data de ida no futuro')

        return departure_date

    def clean_return_date(self):
        return_date = self.cleaned_data['return_date']

        if return_date > now().date():
            self.add_error('return_date', 'Data da volta no futuro')

        return return_date

    def clean(self):
        cleaned_data = super(TripCreateForm, self).clean()

        departure_date = cleaned_data['departure_date']
        return_date = cleaned_data['return_date']

        if departure_date > return_date:
            self.add_error('departure_date', 'A data da ida não pode ser depois da volta')

        return cleaned_data


class ComorbidityCreateForm(forms.ModelForm):
    class Meta:
        model = models.Comorbidity
        fields = '__all__'
        widgets = {
            'type': CheckboxSelectMultiple
        }


SymptomInlineFormset = inlineformset_factory(models.Atendimento, model=models.Symptom, form=SymptomCreateForm, extra=1)

TripInlineFormset = inlineformset_factory(models.Atendimento, models.Trip, form=TripCreateForm, extra=1)

ComorbidityInlineFormset = inlineformset_factory(models.Atendimento, models.Comorbidity, form=ComorbidityCreateForm,
                                                 extra=1)
