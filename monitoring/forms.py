from datetime import datetime

from django import forms
from django.forms import inlineformset_factory
from django.utils import timezone
from django.utils.timezone import now

from monitoring import choices
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
            'symptom': forms.HiddenInput(),
            'label': forms.HiddenInput(),
            'onset': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

    label = forms.CharField(widget=forms.HiddenInput(), required=False, empty_value='')

    def clean_onset(self):
        onset = self.cleaned_data['onset']

        if onset is not None and onset > now().date():
            self.add_error('onset', 'Surgimento de sintoma(s) no futuro')

        return onset


SymptomInlineFormset = inlineformset_factory(models.Atendimento, model=models.Symptom, form=SymptomCreateForm,
                                             extra=len(choices.symptoms), can_delete=False)


class TripCreateForm(forms.ModelForm):
    class Meta:
        model = models.Trip
        fields = '__all__'
        widgets = {
            'profile': forms.HiddenInput(),
            'departure_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'return_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'country': forms.RadioSelect()
        }

    def clean_departure_date(self):
        departure_date = self.cleaned_data['departure_date']

        if departure_date is not None and departure_date > timezone.now().date():
            self.add_error('departure_date', 'Data de ida no futuro')

        return departure_date

    def clean_return_date(self):
        return_date = self.cleaned_data['return_date']

        if return_date is not None and return_date > timezone.now().date():
            self.add_error('return_date', 'Data da volta no futuro')

        return return_date

    def clean(self):
        cleaned_data = super(TripCreateForm, self).clean()

        departure_date = cleaned_data['departure_date']
        return_date = cleaned_data['return_date']

        if departure_date is not None and return_date is not None and departure_date > return_date:
            self.add_error('departure_date', 'A data da ida não pode ser depois da volta')

        return cleaned_data


TripInlineFormset = inlineformset_factory(models.Profile, models.Trip, form=TripCreateForm, extra=1)


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        exclude = ['account']
        widgets = {
            'birth_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']

        if birth_date > timezone.now().date():
            error = 'Data de nascimento após %s inválida' % datetime.strftime(timezone.now().date(), '%d/%m/%Y')
            self.add_error('birth_date', error)

        return birth_date


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = '__all__'
        widgets = {
            'postal_code': forms.TextInput(attrs={'class': 'postal-code-field'}),
            'complement': forms.Textarea(attrs={'rows': 2}),
            'profile': forms.HiddenInput()
        }


AddressFormset = inlineformset_factory(models.Profile, models.Address, form=AddressCreateForm, extra=0, can_delete=True)


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'
