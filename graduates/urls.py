from django.urls import path
from . import views


urlpatterns = [
    path("mezunlar", views.graduates, name="graduates"),
    path("kategori/<slug:slug>", views.graduates_by_category, name="graduates_by_category"),
    path("mezun-detay/<slug:slug>", views.get_graduate_detail, name="graduate_detail"),
]