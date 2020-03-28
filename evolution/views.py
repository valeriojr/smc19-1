from django.shortcuts import render
from django.views import generic
from django.contrib.auth import mixins


class GraphEvolution(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'evolution/graph_evolution.html'
