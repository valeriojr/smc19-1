from django import forms
from django.forms import inlineformset_factory

from . import models


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = models.Atendimento
        fields = '__all__'
        labels = {
            'profile': 'Paciente'
        }


SymptomInlineFormset = inlineformset_factory(models.Atendimento, models.Symptom, fields='__all__', extra=1)

TripInlineFormset = inlineformset_factory(models.Atendimento, models.Trip, fields='__all__', extra=1)

ComorbidityInlineFormset = inlineformset_factory(models.Atendimento, models.Comorbidity, fields='__all__', extra=1)
