import json

from django.shortcuts import render
from django.views import generic
from django.contrib.auth import mixins


class PredictionHub(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'prediction_hub.html'
