from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    inventory = models.PositiveIntegerField(verbose_name='Inventory')

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    no_of_guests = models.PositiveIntegerField(verbose_name='Number Of Guests')
    booking_date = models.DateTimeField(verbose_name='Booking Date', null=False)

    def __str__(self) -> str:
        return f'{self.name} : {self.booking_date}'