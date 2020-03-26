from django.contrib import messages
from django.contrib.auth import mixins
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from monitoring import choices
from . import forms
from . import models


# Create your views here.


class IndexProfile(mixins.LoginRequiredMixin, generic.ListView):
    model = models.Profile
    template_name = 'monitoring/index_profile.html'


class CreateProfile(mixins.LoginRequiredMixin, generic.CreateView):
    form_class = forms.ProfileForm
    template_name = 'monitoring/new_profile.html'
    success_url = reverse_lazy('monitoring:index_profile')


class GetProfile(mixins.LoginRequiredMixin, generic.DetailView):
    model = models.Profile
    template_name = 'monitoring/profile.html'

    def get_context_data(self, **kwargs):
        context = super(GetProfile, self).get_context_data(**kwargs)

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

        return context


class UpdateProfile(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Profile
    form_class = forms.ProfileForm

    def get_success_url(self):
        return reverse('monitoring:get_profile', args=[self.kwargs['pk']])


class DeleteProfile(mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Profile
    success_url = reverse_lazy('monitoring:index_profile')


class CreateAddress(mixins.LoginRequiredMixin, generic.CreateView):
    form_class = forms.AddressForm

    def get_success_url(self):
        return reverse('monitoring:get_profile', args=[self.kwargs['profile']])


class UpdateAddress(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Address
    form_class = forms.AddressForm

    def get_success_url(self):
        return reverse('monitoring:get_profile', args=[self.kwargs['profile']])


class DeleteAddress(mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Address

    def get_success_url(self):
        return reverse('monitoring:get_profile', args=[self.kwargs['profile']])


class CadastrarAtendimento(mixins.LoginRequiredMixin, generic.CreateView):
    form_class = forms.AtendimentoCreateForm
    template_name = 'monitoring/cadastrar_atendimento.html'

    def get_context_data(self, **kwargs):
        context = super(CadastrarAtendimento, self).get_context_data(**kwargs)

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
            self.object = form.save(commit=False)
            self.object.save()

            for formset in symptom_formset:
                instance = formset.save(commit=False)
                if instance.onset != None:
                    instance.atendimento = self.object
                    instance.save()

            messages.success(self.request, 'Atendimento cadastrado com sucesso!')

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(CadastrarAtendimento, self).form_invalid(form)

    def get_success_url(self):
        return reverse('monitoring:index_profile')


class CreateTrip(mixins.LoginRequiredMixin, generic.CreateView):
    form_class = forms.TripForm

    def get_success_url(self):
        return reverse('monitoring:get_profile', args=[self.kwargs['profile']])

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return HttpResponseRedirect(self.get_success_url())


class UpdateTrip(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Trip
    form_class = forms.TripForm

    def get_success_url(self):
        return reverse_lazy('monitoring:index_profile')


class DeleteTrip(mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Trip

    def get_success_url(self):
        return reverse('monitoring:get_profile', args=[self.kwargs['profile']])
