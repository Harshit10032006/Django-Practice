from django.contrib import admin
from .models  import Youtubeuser
# Register your models here.
from django.core.cache import cache
from django.contrib import messages

@admin.action(description='Clear user Cache')
def clear_cache(modeladmin,request,queryset):
    cache.delete('users_data')
    messages.success(request, 'Cache cleared successfully!')


@admin.register(Youtubeuser)
class YoutubeuserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribers')
    list_filter = ('subscribers',)
    search_fields = ('name', 'email')
    ordering = ('name',)
    actions = [clear_cache]

