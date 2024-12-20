from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","token","image","is_verified")

admin.site.register(Profile, ProfileAdmin)