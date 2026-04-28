from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'year', 'price_per_day', 'available', 'location']
    list_filter = ['available', 'transmission', 'fuel_type', 'location']
    search_fields = ['make', 'model']