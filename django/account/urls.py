from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path("csrf/", views.get_csrf, name="api-csrf"),
    path("login/", views.loginView, name="login-view"),
]

