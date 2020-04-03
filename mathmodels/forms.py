from django import forms
from . import choices


class SirSeirForm(forms.Form):
    N = forms.IntegerField(
        help_text='População total',
        initial=1000000,
        widget=forms.NumberInput(attrs={'step': '1000', 'min': '0'}),
        required=True
        )

    S0 = forms.FloatField(
        label='S0',
        help_text='Porcentagem inicial de suscetíveis',
        initial='0.99995',
        widget=forms.NumberInput(attrs={'step': '0.0000001', 'min': '0', 'max':'1'}),
        required=True
        )
    
    E0 = forms.FloatField(
        label='E0',
        help_text='Porcentagem inicial de expostos',
        initial='0.0',
        widget=forms.NumberInput(attrs={'step': '0.0000001', 'min': '0', 'max':'1'}),
        required=True
        )

    I0 = forms.FloatField(
        label='I0',
        help_text='Porcentagem inicial de infectados',
        initial='0.00005',
        widget=forms.NumberInput(attrs={'step': '0.0000001', 'min': '0', 'max':'1'}),
        required=True
        )

    R0 = forms.FloatField(
        label='R0',
        help_text='Porcentagem inicial de recuperados',
        initial='0.0',
        widget=forms.NumberInput(attrs={'step': '0.0000001', 'min': '0', 'max':'1'}),
        required=True
        )

    alpha = forms.FloatField(
        label='alpha',
        help_text='Parâmetro alpha (SEIR)',
        initial='0.2',
        widget=forms.NumberInput(attrs={'step': '0.01'}),
        required=True
        )

    beta = forms.FloatField(
        label='beta',
        help_text='Parâmetro beta',
        initial='1.75',
        widget=forms.NumberInput(attrs={'step': '0.01'}),
        required=True
        )

    gamma = forms.FloatField(
        label='gamma',
        help_text='Parâmetro gamma',
        initial='0.5',
        widget=forms.NumberInput(attrs={'step': '0.01'}),
        required=True
        )

    rho = forms.FloatField(
        label='rho',
        help_text='Parâmetro rho (distanciamento social)',
        initial='1.0',
        widget=forms.NumberInput(attrs={'step': '0.01', 'min': '0.0', 'max':'1.0'}),
        required=True
        )

    days = forms.IntegerField(
        label='Dias',
        help_text='Dias da simulação',
        initial='120',
        widget=forms.NumberInput(attrs={'step': '1', 'min': '0'}),
        required=True
        )

    model = forms.ChoiceField(
        label='Modelo',
        choices=choices.model_type
        )
