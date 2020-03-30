from django.shortcuts import render
from django.views import generic
from django.views import View
from django.contrib.auth import mixins

import csv
from django.http import HttpResponse


class DataGraphEvolution(mixins.LoginRequiredMixin, View):
    def get(self, request):
        print(request.GET)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="dataset.csv"'

        writer = csv.writer(response)
        writer.writerow(['date','value'])
        for i in range(1,32):
            writer.writerow(['2019-03-{}'.format(i),1.2**i])
        

        return response

class GraphEvolution(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'evolution/graph_evolution.html'
