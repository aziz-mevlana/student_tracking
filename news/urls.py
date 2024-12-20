from django.urls import path
from . import views
# http://127.0.0.1:8000/         => index
# http://127.0.0.1:8000/index    => index
# http://127.0.0.1:8000/news     => news
# http://127.0.0.1:8000/news/3   => news-details

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("news", views.news, name="news"),
    path("news/<slug:slug>", views.news_details, name="news_details"), #degisken sayfa cagirma
    path("deneme", views.deneme, name="deneme"),
    
]