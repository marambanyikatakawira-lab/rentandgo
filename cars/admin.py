from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price_per_day', 'is_available')
    list_filter = ('is_available', 'transmission', 'fuel_type', 'location')
    search_fields = ('make', 'model')

admin.site.register(Car, CarAdmin)