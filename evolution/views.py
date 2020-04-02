from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from django.views import View
from django.contrib.auth import mixins

import csv
from django.http import HttpResponse, JsonResponse

from monitoring.models import State,City,Neighbourhood, Monitoring

from django.utils import dateparse, timezone


class DataGraphEvolution(mixins.LoginRequiredMixin, View):
    def get(self, request):
        if 'popular_select' in request.GET:
            city = request.GET.get('CIDADE','')
            neighbourhood = request.GET.get('BAIRRO','')

            TODOS = [{'value':'TODOS', 'text':'TODOS'}]
            FETCHED = []

            if city == 'ELEMENTOS':
                FETCHED = [{'value':u.name, 'text': u.name} for u in City.objects.all()]

            elif neighbourhood == 'ELEMENTOS':
                city = get_object_or_404(City, name=city)
                FETCHED = [{'value':u.name, 'text': u.name} for u in get_list_or_404(Neighbourhood,city=city)]
            
            return JsonResponse(TODOS + FETCHED, safe=False)
        
        if 'ver_grafico' in request.GET:
            city = request.GET.get('CIDADE','')
            neighbourhood = request.GET.get('BAIRRO','')
            status = request.GET.get('STATUS','')
            initial_date = dateparse.parse_date(request.GET.get('INICIAL','2020-01-01'))
            final_date = request.GET.get('FINAL', str(timezone.now().date()))

            initial_date = request.GET.get('INICIAL')
            if not len(initial_date):
                initial_date = Monitoring.objects.all().order_by('id')[0].created.date().__str__()
            final_date = request.GET.get('FINAL')
            if not len(final_date):
                final_date = Monitoring.objects.all().order_by('-id')[0].created.date().__str__()

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="dataset.csv"'

            writer = csv.writer(response)
            writer.writerow(['date','value'])
            for i in range(1,32):
                writer.writerow(['2019-03-{}'.format(i),1.2**i])
            
            return response

class GraphEvolution(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'evolution/graph_evolution.html'
