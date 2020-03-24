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
            context['address_formset'] = forms.AddressFormset(self.request.POST, instance=self.object)
        else:
            context['address_formset'] = forms.AddressFormset()

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        address_formset = context['address_formset']

        if address_formset.is_valid():
            self.object = form.save(commit=False)
            self.object.set_password(form.cleaned_data['password'])
            self.object.save()

            addresses = address_formset.save(commit=False)
            for address in addresses:
                address.profile = self.object
                address.save()

        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(SignUp, self).form_invalid(form)
