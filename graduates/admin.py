from django.contrib import admin
from .models import GraduatingStudents,Category


class GraduatingStudentsAdmin(admin.ModelAdmin):
    list_display = ("name","surname","graduation_date","category","slug",)
    list_filter = ("category",)
    


admin.site.register(GraduatingStudents,GraduatingStudentsAdmin)
admin.site.register(Category)


