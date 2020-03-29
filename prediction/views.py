import json

from django.shortcuts import render
from django.views import generic
from django.contrib.auth import mixins


class PredictionHub(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'prediction_hub.html'

def create_health_centers():
    health_centers = []
    with open('static/data/unidadesdesaude.json', 'r') as json_file:
        data = json.load(json_file)

        for feat in data['features']:
            center_name = feat['properties']['Nome']
            address = feat['properties']['Endereço']
            latitude = feat['geometry']['coordinates'][0]
            longitude = feat['geometry']['coordinates'][1]
            
            hc = HealthCenters(
                center_name=center_name,
                address=address,
                latitude=latitude,
                longitude=longitude
            )

            health_centers.append(hc)

        return health_centers
