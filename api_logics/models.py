from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class pickUpClass(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    bus_stop = models.CharField(max_length=250)
    address = models.CharField(max_length=500, default='Nan', blank=True, null=True)
    number_of_item = models.PositiveIntegerField()
    message = models.TextField()
    # other useful filed
    date = models.DateField(auto_now=False, auto_now_add=True)
    time = models.TimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = 'Pick Ups'

class testimonialClass(models.Model):
    full_name = models.CharField(max_length=100)
    passport = models.ImageField(upload_to='image', height_field=None, width_field=None, max_length=None)
    testimony = models.TextField()

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = 'Testimonials'

class contactClass(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Contacts'
    
