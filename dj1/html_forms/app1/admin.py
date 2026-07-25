from django.contrib import admin
from .models import contact

# Register your models here.

@admin.register(contact)

class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'mobile')