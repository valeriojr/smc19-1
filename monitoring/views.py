from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import mixins

from . import forms

# Create your views here.


class Home(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'monitoring/home.html'


class CadastrarAtendimento(mixins.LoginRequiredMixin, generic.CreateView):
    form_class = forms.AtendimentoForm
    success_url = reverse_lazy('monitoring:home')
    template_name = 'monitoring/cadastrar_atendimento.html'

    def form_valid(self, form):
        return super(CadastrarAtendimento, self).form_valid(form)

    def form_invalid(self, form):
        for error in form.errors:
            messages.error(self.request, error)

        return super(CadastrarAtendimento, self).form_invalid(form)
