from django.contrib import admin
from .models import task

# Register your models here.

@admin.register(task)
class taskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')