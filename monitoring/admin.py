from django.contrib import admin
from bitfield import BitField
from bitfield.forms import BitFieldCheckboxSelectMultiple

from . import models

# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.Address)
admin.site.register(models.Monitoring)
admin.site.register(models.Symptom)
admin.site.register(models.Trip)