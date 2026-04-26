from django.contrib import admin

from .models import Medecin, Patient, RendezVous

admin.site.register(Medecin)
admin.site.register(Patient)
admin.site.register(RendezVous)
