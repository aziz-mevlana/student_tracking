from django.contrib import admin
from .models import News,Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug",)
    list_editable = ("is_active","is_home",)
    search_fields = ("title","description",)
    ordering = ("published_date",)
    
    
    
admin.site.register(News, NewsAdmin)
admin.site.register(Category)
