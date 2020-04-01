from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import  redirect
from . import forms


# Create your views here.


class SignUp(generic.CreateView):
    form_class = forms.AccountCreationForm
    template_name = 'sign-up.html'

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(SignUp, self).form_invalid(form)

    def form_valid(self, form):
        #Aqui é feita outras validações que não são possíveis no form.clean()
        user = self.request.user
        user_profile = form.cleaned_data['user_profile']
        health_center = form.cleaned_data['health_center']
        if user.user_profile == 'AU':#atendente de uma unidade tentou criar um usuário
            messages.error(self.request, "Você não tem permissão para criar outros usuários.")
        elif (user.user_profile == 'AD') and (user_profile == 'SS'):#tentou criar um perfil Secretaria de saude
            messages.error(self.request, "Você não pode criar esse tipo de usuário.")
        elif (user.user_profile == 'AD') and (health_center != user.health_center):#tentou criar usuário de outra unidade
            messages.error(self.request, "Você não pode criar usuários de outras unidades.")
        else:
            messages.success(self.request, "Usuário criado com sucesso.")
        return redirect('accounts:sign-up')