from django.contrib import admin
from .models import Location, ContactTicket


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'address']



@admin.register(ContactTicket)
class ContactTicketAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'subject',
                    'message', 'created',
                    'updated',]

