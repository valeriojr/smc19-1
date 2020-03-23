from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from . import forms


# Create your views here.


class SignUp(generic.CreateView):
    form_class = forms.ProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign-up.html'

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        if self.request.POST:
            context['address_form'] = forms.AddressFormset(self.request.POST, instance=self.object)
            context['trip_form'] = forms.TripFormset(self.request.POST, instance=self.object)
            context['symptom_form'] = forms.SymptomFormset(self.request.POST, instance=self.object)
            context['comorbidity_form'] = forms.ComorbidityFormset(self.request.POST, instance=self.object)
        else:
            context['address_form'] = forms.AddressFormset()
            context['trip_form'] = forms.TripFormset()
            context['symptom_form'] = forms.SymptomFormset()
            context['comorbidity_form'] = forms.ComorbidityFormset()

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        address_formset = context['address_form']
        trip_formset = context['trip_form']
        symptom_formset = context['symptom_form']
        comorbidity_formset = context['comorbidity_form']

        if form.is_valid() and address_formset.is_valid() and trip_formset.is_valid() and comorbidity_formset.is_valid():
            self.object = form.save(commit=False)
            self.object.set_password(form.cleaned_data['password'])
            self.object.save()

            addresses = address_formset.save(commit=False)
            for address in addresses:
                address.profile = self.object
                address.save()

            trips = trip_formset.save(commit=False)
            for trip in trips:
                trip.profile = self.object
                trip.save()

            symptoms = symptom_formset.save(commit=False)
            for symptom in symptoms:
                symptom.profile = self.object
                symptom.save()

            comorbidities = comorbidity_formset.save(commit=False)
            for comorbidity in comorbidities:
                comorbidity.profile = self.object
                comorbidity.save()

        messages.success(self.request, form.errors)

        return HttpResponseRedirect(self.success_url)


    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(SignUp, self).form_invalid(form)
