from django.shortcuts import render
from django.views import View

from django.views import generic
from django.views import View
from django.contrib.auth import mixins


class SirSeirMathModel(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'mathmodels/sir_seir_math_model.html'