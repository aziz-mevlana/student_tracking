from django.urls import path, include
from .import views


urlpatterns = [
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path('verify-account/', views.verify_account, name='verify_account'),
    path("logout", views.logout_request, name="logout"),
    path("profile", views.profile_request, name="profile" ),
]
