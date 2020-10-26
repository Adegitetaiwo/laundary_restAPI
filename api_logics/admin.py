from django.contrib import admin
from .models import pickUpClass, contactClass, testimonialClass
# Register your models here.

@admin.register(pickUpClass)
class pickUpClassAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'bus_stop', 'number_of_item', 'date', 'time']
    readonly_fields = ['date', 'time']
    list_filter = ['bus_stop', 'number_of_item', 'date']

@admin.register(contactClass)
class contactClassAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'email']
    readonly_fields = ['first_name','last_name', 'email', 'subject', 'message']

admin.site.register(testimonialClass)