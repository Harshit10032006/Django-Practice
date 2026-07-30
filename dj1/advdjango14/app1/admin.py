from django.contrib import admin
from .models import user_list

# Register your models here.

@admin.register(user_list)
class user_listAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)