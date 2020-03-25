from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from . import forms


# Create your views here.


class SignUp(generic.CreateView):
    form_class = forms.AccountCreationForm
    template_name = 'sign-up.html'

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(SignUp, self).form_invalid(form)

    def get_success_url(self):
        return self.request.GET.get('next', reverse('login'))
