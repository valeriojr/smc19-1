from django.contrib import messages
from django.contrib.auth import mixins
from django.db.models import Count, Q, Avg
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django import forms


from monitoring import choices
from . import models

from django.shortcuts import render

from monitoring import utils

class HealthCenterStatusCreate(mixins.LoginRequiredMixin, generic.CreateView):
    # form_class = forms.HealthCenterStatusForm
    model = models.HealthCenterStatus
    
    fields = ('health_center', 'beds', 'icus', 'respirators', 'occupied_beds', 'occupied_icus', 'occupied_respirators',)
    
    template_name = 'prediction/prediction_hub.html'
    success_url = reverse_lazy('prediction:prediction_hub')
    
    def get_form(self, form_class=None):
        form = super(HealthCenterStatusCreate, self).get_form(form_class)
        form.fields['health_center'].widget = forms.HiddenInput()
        return form
    
    def get_initial(self):
        init = super(HealthCenterStatusCreate, self).get_initial()
        init['health_center'] = self.request.user.health_center
        return init

    def form_valid(self, form):
        utils.create_log(self.request, 'C', 'RE')
        messages.success(self.request, 'Status da unidade atualizado.')
        return super(HealthCenterStatusCreate, self).form_valid(form)
