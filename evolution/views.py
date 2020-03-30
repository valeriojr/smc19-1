from django.shortcuts import render
from django.views import generic
from django.views import View
from django.contrib.auth import mixins

import csv
from django.http import HttpResponse, JsonResponse

from monitoring.models import State,City,Neighbourhood


class DataGraphEvolution(mixins.LoginRequiredMixin, View):
    def get(self, request):
        state = request.GET.get('UF','')
        city = request.GET.get('CIDADE','')
        neighbourhood = request.GET.get('BAIRRO','')
        status = request.GET.get('STATUS','')

        TODOS = [{'value':'TODOS', 'text':'TODOS'}]

        if request.GET.get('UF','') == 'ELEMENTOS':
            FETCHED = [{'value':u.name, 'text': u.name} for u in State.objects.all()]
            return JsonResponse(TODOS + FETCHED, safe=False)

        if request.GET.get('CIDADE','') == 'ELEMENTOS':
            state = State.objects.get(name=request.GET.get('UF',''))
            FETCHED = [{'value':u.name, 'text': u.name} for u in City.objects.filter(state=state)]
            return JsonResponse(TODOS + FETCHED, safe=False)

        if request.GET.get('BAIRRO','') == 'ELEMENTOS':
            state = State.objects.get(name=request.GET.get('UF',''))
            city = City.objects.get(state=state, name=request.GET.get('CIDADE',''))
            FETCHED = [{'value':u.name, 'text': u.name} for u in Neighbourhood.objects.filter(city=city)]
            return JsonResponse(TODOS + FETCHED, safe=False)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="dataset.csv"'

        writer = csv.writer(response)
        writer.writerow(['date','value'])
        for i in range(1,32):
            writer.writerow(['2019-03-{}'.format(i),1.2**i])
        

        return response

class GraphEvolution(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'evolution/graph_evolution.html'
