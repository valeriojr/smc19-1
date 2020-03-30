from django.shortcuts import render, get_object_or_404, get_list_or_404
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

        if state == 'ELEMENTOS':
            FETCHED = [{'value':u.name, 'text': u.name} for u in State.objects.all()]
            return JsonResponse(TODOS + FETCHED, safe=False)

        elif city == 'ELEMENTOS':
            state = get_object_or_404(State, name=state)
            FETCHED = [{'value':u.name, 'text': u.name} for u in get_list_or_404(City,state=state)]
            return JsonResponse(TODOS + FETCHED, safe=False)

        elif neighbourhood == 'ELEMENTOS':
            state = get_object_or_404(State, name=state)
            city = get_object_or_404(City, state=state, name=city)
            FETCHED = [{'value':u.name, 'text': u.name} for u in get_list_or_404(Neighbourhood,city=city)]
            return JsonResponse(TODOS + FETCHED, safe=False)
        
        if 'ver_grafico' in request.GET:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="dataset.csv"'

            writer = csv.writer(response)
            writer.writerow(['date','value'])
            for i in range(1,32):
                writer.writerow(['2019-03-{}'.format(i),1.2**i])
            
            return response

class GraphEvolution(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'evolution/graph_evolution.html'
