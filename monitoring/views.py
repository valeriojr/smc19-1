from django.contrib import messages
from django.contrib.auth import mixins
from django.db.models import Count, Q, F
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from monitoring import choices
from . import forms
from . import models


# Create your views here.

class Index(mixins.LoginRequiredMixin, generic.ListView):
    model = models.Profile
    template_name = 'monitoring/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context['monitorings'] = models.Monitoring.objects
        context['monitoring_create_form'] = forms.MonitoringForm()
        symptoms_initial = [{'symptom': symptom[0], 'label': symptom[1]} for symptom in choices.symptoms]
        context['symptom_formset'] = forms.SymptomInlineFormset(initial=symptoms_initial)

        return context


class Map(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'monitoring/map.html'

    def get_context_data(self, **kwargs):
        context = super(Map, self).get_context_data(**kwargs)

        query = {
            'suspect_cases': Count(F('suspect'), filter=(Q(suspect=True) & ~Q(result='PO'))),
            'confirmed_cases': Count(F('result'), filter=Q(result='PO'))
        }
        stats_per_city = models.Monitoring.objects.values('profile__address__city', 'profile').filter().annotate(**query)

        context['stats'] = {
            'total_profiles': models.Monitoring.objects.values('profile').count(),
            'total': models.Monitoring.objects.values('profile').filter().aggregate(**query),
            'cities': {
                stat['profile__address__city'] if 'profile__address__city' in stat else stat[
                    'profile__address__neighbourhood']: stat for stat in
                stats_per_city}
        }

        return context


# Profile

class ProfileCreate(mixins.LoginRequiredMixin, generic.CreateView):
    form_class = forms.ProfileForm
    template_name = 'monitoring/new_profile.html'
    success_url = reverse_lazy('monitoring:index')


class ProfileDetail(mixins.LoginRequiredMixin, generic.DetailView):
    model = models.Profile
    template_name = 'monitoring/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)

        context['update_profile_form'] = forms.ProfileForm(instance=self.object)

        context['address_form'] = forms.AddressForm(data={
            'profile': self.object.id
        })

        context['update_address_forms'] = [forms.AddressForm(instance=address) for address in
                                           self.object.address_set.all()]

        context['create_trip_form'] = forms.TripForm(data={
            'profile': self.object.id
        })

        context['update_trip_forms'] = [forms.TripForm(instance=trip) for trip in
                                        self.object.trip_set.all()]

        comorbidities = []
        for comorbidity in self.object.comorbidities:
            comorbidities.append({
                'label': self.object.comorbidities.get_label(comorbidity[0]),
                'set': comorbidity[1]
            })

        context['comorbidities'] = comorbidities

        return context


class ProfileUpdate(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Profile
    form_class = forms.ProfileForm

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('monitoring:profile-detail', args=[self.kwargs['pk']])


class ProfileDelete(mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Profile
    success_url = reverse_lazy('monitoring:index')


# Address

class AddressCreate(mixins.LoginRequiredMixin, generic.CreateView):
    form_class = forms.AddressForm

    def get_success_url(self):
        return reverse('monitoring:profile-detail', args=[self.kwargs['profile']])


class AddressUpdate(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Address
    form_class = forms.AddressForm

    def get_success_url(self):
        return reverse('monitoring:profile-detail', args=[self.kwargs['profile']])


class AddressDelete(mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Address

    def get_success_url(self):
        return reverse('monitoring:profile-detail', args=[self.kwargs['profile']])


# Monitoring

class MonitoringDetail(mixins.LoginRequiredMixin, generic.DetailView):
    model = models.Monitoring

    def get_context_data(self, **kwargs):
        context = super(MonitoringDetail, self).get_context_data(**kwargs)

        # Formulário de edição do atendimento atual
        context['monitoring_update_form'] = forms.MonitoringForm(instance=self.object)

        symptoms_initial = []
        for symptom in choices.symptoms:
            s = models.Symptom.objects.filter(symptom=symptom[0])
            if len(s) > 0:
                symptoms_initial.append({
                    'symptom': symptom[0],
                    'label': symptom[1],
                    'onset': s[0].onset
                })
            else:
                symptoms_initial.append({
                    'symptom': symptom[0],
                    'label': symptom[1]
                })

        else:
            context['symptom_formset'] = forms.SymptomInlineFormset(initial=symptoms_initial)

        exposures = []
        for exposure in self.object.virus_exposure:
            exposures.append({
                'label': self.object.virus_exposure.get_label(exposure[0]),
                'set': exposure[1]
            })

        context['exposures'] = exposures

        return context


class MonitoringCreate(mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Monitoring
    form_class = forms.MonitoringForm

    def get_context_data(self, **kwargs):
        context = super(MonitoringCreate, self).get_context_data(**kwargs)

        symptoms_initial = [{'symptom': symptom[0], 'label': symptom[1]} for symptom in choices.symptoms]

        if self.request.POST:
            context['symptom_formset'] = forms.SymptomInlineFormset(self.request.POST, initial=symptoms_initial)
        else:
            context['symptom_formset'] = forms.SymptomInlineFormset(initial=symptoms_initial)

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        symptom_formset = context['symptom_formset']

        if symptom_formset.is_valid():
            self.object = form.save(commit=True)

            for formset in symptom_formset:
                instance = formset.save(commit=False)
                if instance.onset != None:
                    instance.monitoring = self.object
                    instance.save()

            messages.success(self.request, 'Atendimento cadastrado com sucesso!')

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(MonitoringCreate, self).form_invalid(form)

    def get_success_url(self):
        return reverse('monitoring:index')


class MonitoringUpdate(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Monitoring
    form_class = forms.MonitoringForm

    def get_context_data(self, **kwargs):
        context = super(MonitoringUpdate, self).get_context_data(**kwargs)

        if self.request.POST:
            symptoms_initial = [{'symptom': symptom[0], 'label': symptom[1]} for symptom in choices.symptoms]
            context['symptom_formset'] = forms.SymptomInlineFormset(self.request.POST, initial=symptoms_initial)

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        symptom_formset = context['symptom_formset']

        if symptom_formset.is_valid():
            self.object = form.save(commit=True)

            for formset in symptom_formset:
                instance = formset.save(commit=False)
                symptoms = self.object.symptom_set.filter(symptom=instance.symptom)
                if len(symptoms) == 1:
                    if instance.onset is not None:
                        symptoms[0].onset = instance.onset
                        symptoms[0].save()
                    else:
                        symptoms[0].delete()
                else:
                    if instance.onset is not None:
                        instance.monitoring = self.object
                        instance.save()

            messages.success(self.request, 'Atendimento atualizado com sucesso!')

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('monitoring:monitoring-detail', args=[self.kwargs['pk']])


class MonitoringDelete(mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Monitoring

    def get_success_url(self):
        return reverse('monitoring:index')


# Trip

class TripCreate(mixins.LoginRequiredMixin, generic.CreateView):
    form_class = forms.TripForm

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('monitoring:profile-detail', args=[self.kwargs['profile']])


class TripUpdate(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Trip
    form_class = forms.TripForm

    def get_success_url(self):
        return reverse_lazy('monitoring:index')


class TripDelete(mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Trip

    def get_success_url(self):
        return reverse('monitoring:profile-detail', args=[self.kwargs['profile']])
