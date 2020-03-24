from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Atendimento)
admin.site.register(models.Symptom)
admin.site.register(models.Trip)
admin.site.register(models.Comorbidity)
