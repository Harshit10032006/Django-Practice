from django.contrib import admin
from .models import user_profile

# Register your models here.

@admin.register(user_profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscriber')
    list_filter = ('subscriber',)
    search_fields = ('name', 'email')
    ordering = ('name',)