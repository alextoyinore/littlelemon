from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=50, unique=True)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.name}'

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

    def __repr__(self):
        return f'{self.title} : {str(self.price)}'