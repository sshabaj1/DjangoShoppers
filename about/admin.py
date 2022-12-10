from django.contrib import admin
from .models import AboutComponent


@admin.register(AboutComponent)
class AboutComponentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'video',
                    'image', 'available']
    list_editable = ['video', 'image', 'available']
