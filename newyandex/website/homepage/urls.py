from django.urls import path

from . import views

urlpatterns = [
    path("homepage/", views.HomePage.as_view())
]