from django.urls import path
from . import views


urlpatterns = [
    path("graduates", views.graduates, name="graduates"),
    path("category", views.graduates_by_category, name="graduates_by_category"),
    path("graduates/<slug:slug>", views.graduates_by_category, name="graduates_by_category"), #degisken sayfa cagirma
]