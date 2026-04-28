from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    description = models.TextField(blank=True)
    seats = models.IntegerField(default=5)
    transmission = models.CharField(max_length=20, choices=[
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ], default='Automatic')
    fuel_type = models.CharField(max_length=20, choices=[
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ], default='Petrol')
    location = models.CharField(max_length=100, default='Harare')

    def _str_(self):
        return f"{self.year} {self.make} {self.model}"