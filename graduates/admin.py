from django.contrib import admin
from .models import GraduatingStudents, Category


@admin.register(GraduatingStudents)
class GraduatingStudentsAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "graduation_date", "category", "email")
    list_filter = ("category", "graduation_date")
    search_fields = ("name", "surname", "email", "description")
    readonly_fields = ("slug",)
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('name', 'surname', 'img', 'graduation_date', 'category', 'slug')
        }),
        ('İletişim Bilgileri', {
            'fields': ('email', 'website')
        }),
        ('Sosyal Medya', {
            'fields': ('linkedin', 'github', 'twitter', 'instagram')
        }),
        ('Detaylı Bilgiler', {
            'fields': ('description', 'cv_file')
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    readonly_fields = ("slug",)


