from django.contrib import admin

from .models import HealthCenter, HealthCenterStatus

admin.site.register(HealthCenter)
admin.site.register(HealthCenterStatus)
