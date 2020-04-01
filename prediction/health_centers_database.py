import json

from models import HealthCenter

if __name__ == "__main__":
    with open('static/data/unidadessaude.json') as f:
        data = json.load(f)

    health_units = []
    
    for d in data:
        center_name, latitude, longitude = d['no_fantasia'], d['lat'], d['long']
        health_units.append(
            HealthCenter(center_name=center_name, latitude=latitude, longitude=longitude)
        )
    
    HealthCenter.objects.bulk_create(health_units)