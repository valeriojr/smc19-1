from django import forms
from django.forms import inlineformset_factory, CheckboxSelectMultiple

from . import models


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = models.Atendimento
        fields = '__all__'
        labels = {
            'profile': 'Paciente'
        }


SymptomInlineFormset = inlineformset_factory( models.Atendimento, models.Symptom, 
  fields='__all__', 
  extra=1,
  widgets = {"symptom": CheckboxSelectMultiple, "onset": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})})

TripInlineFormset = inlineformset_factory(models.Atendimento, models.Trip, fields='__all__', extra=1,
                                          widgets={
                                              'departure_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
                                              'return_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
                                              'country': CheckboxSelectMultiple
                                          })

ComorbidityInlineFormset = inlineformset_factory(models.Atendimento, models.Comorbidity, 
  fields='__all__', extra=1, widgets = {"type": CheckboxSelectMultiple})
