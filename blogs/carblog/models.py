from django.db import models

class Car(models.Model):
    make=models.CharField(max_length=50, choices=[('Toyota', 'Toyota'), ('Honda', 'Honda')])
    model=models.CharField(blank=True, null=True)
    year=models.PositiveIntegerField(default=2024)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    description=models.TextField(help_text="Enter the description of the car")
    serial_num=models.CharField(unique=True)
    # mileage=models.DecimalField(default=None)
    manu_date=models.DateField(auto_now_add=True)
    # owner=models.ForeignKey('Owner', on_delete=models.SET_NULL, related_name='cars')
    details=models.TextField(blank=True, null=True)

