from django.contrib import messages
from django.contrib.auth import mixins
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from accounts.forms import ProfileCreationForm, AddressFormset
from . import forms


# Create your views here.


class Home(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'monitoring/home.html'


class NewProfile(mixins.LoginRequiredMixin, generic.CreateView):
    form_class = ProfileCreationForm
    template_name = 'monitoring/new_profile.html'

    def get_context_data(self, **kwargs):
        context = super(NewProfile, self).get_context_data(**kwargs)

        if self.request.POST:
            context['address_formset'] = AddressFormset(self.request.POST, instance=self.object)
        else:
            context['address_formset'] = AddressFormset()

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        address_formset = context['address_formset']

        if  address_formset.is_valid():
            self.object = form.save(commit=False)
            self.object.save()

            addresses = address_formset.save(commit=False)
            for address in addresses:
                address.profile = self.object
                address.save()

            messages.success(self.request, 'Paciente %s cadastrado com sucesso!' % self.object.full_name)
        else:
            messages.error(self.request, 'Não foi possível criar o usuário')
            for error in address_formset.errors.items():
                messages.error(self.request, error)

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(NewProfile, self).form_invalid(form)

    def get_success_url(self):
        return self.request.GET.get('next', reverse('login'))


class CadastrarAtendimento(mixins.LoginRequiredMixin, generic.CreateView):
    form_class = forms.AtendimentoForm
    success_url = reverse_lazy('monitoring:home')
    template_name = 'monitoring/cadastrar_atendimento.html'

    def get_context_data(self, **kwargs):
        context = super(CadastrarAtendimento, self).get_context_data(**kwargs)

        if self.request.POST:
            context['symptom_formset'] = forms.SymptomInlineFormset(self.request.POST)
            context['trip_formset'] = forms.TripInlineFormset(self.request.POST, instance=self.object)
            context['comorbidity_formset'] = forms.ComorbidityInlineFormset(self.request.POST, instance=self.object)
        else:
            context['symptom_formset'] = forms.SymptomInlineFormset()
            context['trip_formset'] = forms.TripInlineFormset()
            context['comorbidity_formset'] = forms.ComorbidityInlineFormset()

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        symptom_formset = context['symptom_formset']
        trip_formset = context['trip_formset']
        comorbidity_formset = context['comorbidity_formset']

        if symptom_formset.is_valid() and trip_formset.is_valid() and comorbidity_formset.is_valid():
            self.object = form.save(commit=False)
            self.object.set_password(form.cleaned_data['password'])
            self.object.save()

            for formset in ['symptom_formset', 'trip_formset', 'comorbidity_formset']:
                instances = context[formset].save(commit=False)
                for instance in instances:
                    instance.atendimento = self.object
                    instance.save()

            messages.success(self.request, 'Atendimento %s cadastrado com sucesso!' % self.object.cpf)
        else:
            messages.error(self.request, 'Não foi possível criar o usuário')
            for formset in ['symptom_formset', 'trip_formset', 'comorbidity_formset']:
                messages.error(self.request, context[formset].errors)

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(CadastrarAtendimento, self).form_invalid(form)

    def get_success_url(self):
        return self.request.GET.get('next', reverse('login'))
