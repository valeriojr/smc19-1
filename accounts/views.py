from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from . import forms


# Create your views here.


class SignUp(generic.CreateView):
    form_class = forms.AccountCreationForm
    template_name = 'sign-up.html'

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)

        if self.request.POST:
            context['profile_form'] = forms.ProfileCreationForm(self.request.POST)
            context['address_formset'] = forms.AddressFormset(self.request.POST, instance=self.object)
        else:
            context['profile_form'] = forms.ProfileCreationForm()
            context['address_formset'] = forms.AddressFormset()

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        profile_form = context['profile_form']
        address_formset = context['address_formset']

        if profile_form.is_valid() and address_formset.is_valid():
            self.object = form.save(commit=False)
            self.object.set_password(form.cleaned_data['password'])
            self.object.save()

            profile = profile_form.save(commit=False)
            profile.account = self.object
            profile.save()

            addresses = address_formset.save(commit=False)
            for address in addresses:
                address.profile = profile
                address.save()

            messages.success(self.request, 'Usuário %s cadastrado com sucesso!' % self.object.cpf)
        else:
            messages.error(self.request, 'Não foi possível criar o usuário')
            for error in profile_form.errors.items():
                messages.error(self.request, error)
            for error in address_formset.errors:
                messages.error(self.request, error)

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(SignUp, self).form_invalid(form)

    def get_success_url(self):
        return self.request.GET.get('next', reverse('login'))
