from django.contrib import admin
from .models import HairSalon, Reservations, Services

admin.site.register(HairSalon)
admin.site.register(Reservations)
admin.site.register(Services)