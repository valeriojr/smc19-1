from django import forms
from . import choices


class SirSeirForm(forms.Form):
    N = forms.IntegerField(
        help_text='População total',
        widget=forms.NumberInput(attrs={'step': '1', 'min': '0'}),
        required=True
        )

    S0 = forms.FloatField(
        label='S0',
        help_text='Porcentagem inicial de suscetíveis',
        widget=forms.NumberInput(attrs={'step': '0.000000000001', 'min': '0', 'max':'1'}),
        required=True
        )
    
    E0 = forms.FloatField(
        label='E0',
        help_text='Porcentagem inicial de expostos',
        widget=forms.NumberInput(attrs={'step': '0.000000000001', 'min': '0', 'max':'1'}),
        required=True
        )

    I0 = forms.FloatField(
        label='I0',
        help_text='Porcentagem inicial de infectados',
        widget=forms.NumberInput(attrs={'step': '0.000000000001', 'min': '0', 'max':'1'}),
        required=True
        )

    R0 = forms.FloatField(
        label='R0',
        help_text='Porcentagem inicial de recuperados',
        widget=forms.NumberInput(attrs={'step': '0.000000000001', 'min': '0', 'max':'1'}),
        required=True
        )

    alpha = forms.FloatField(
        label='alpha',
        help_text='Parâmetro alpha (SEIR)',
        widget=forms.NumberInput(attrs={'step': '0.0001'}),
        required=True
        )

    beta = forms.FloatField(
        label='beta',
        help_text='Parâmetro beta',
        widget=forms.NumberInput(attrs={'step': '0.0001'}),
        required=True
        )

    gamma = forms.FloatField(
        label='gamma',
        help_text='Parâmetro gamma',
        widget=forms.NumberInput(attrs={'step': '0.0001'}),
        required=True
        )

    rho = forms.FloatField(
        label='rho',
        help_text='Parâmetro rho (SEIR com isolamento)',
        widget=forms.NumberInput(attrs={'step': '0.0001', 'min': '0', 'max':'1'}),
        required=True
        )

    days = forms.IntegerField(
        label='Dias',
        help_text='Dias da simulação',
        widget=forms.NumberInput(attrs={'step': '1', 'min': '0'}),
        required=True
        )

    model = forms.ChoiceField(
        label='Modelo',
        choices=choices.model_type
        )
