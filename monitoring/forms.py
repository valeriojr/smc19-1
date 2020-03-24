from django import forms

from . import models


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = models.Atendimento
        fields = '__all__'
