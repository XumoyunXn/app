from pyexpat import model
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Davlat"
        verbose_name_plural = "Davlatlar"

    def __str__(self):
        return self.name


class Region(models.Model):
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE)   
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"

    def __str__(self):
        return self.name
    

class Carservice(models.Model):
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)   
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"


    

    def __str__(self):
        return self.name


class Masters(models.Model):
    carservice = models.ForeignKey(Carservice, null=True, blank=True, on_delete=models.CASCADE)   
    images = models.ImageField(upload_to='images/') # Rasm uchun
    name = models.CharField(max_length=255)                   # Ism / Name
    address = models.CharField(max_length=255, blank=True)    # Manzil / Address
    landmark = models.CharField(max_length=255, blank=True)   # Orientir / Landmark
    latitude = models.DecimalField(max_digits=9, decimal_places=6)   # Kenglik
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Uzunlik
    phone = models.CharField(max_length=20, blank=True)       # Telefon
    working_hours = models.CharField(max_length=100, blank=True) # Ish vaqti
    working_days = models.CharField(max_length=50, blank=True)    # Ish kuni
    occupation = models.CharField(max_length=100, blank=True)     # Faoliyati


    class Meta:
        verbose_name = "Usta"
        verbose_name_plural = "Ustalar"
    
    def __str__(self):
        return self.name        