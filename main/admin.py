from django.contrib import admin
from .models import Region, Carservice, Masters, Country, New


admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Carservice)
admin.site.register(Masters)
admin.site.register(New)

