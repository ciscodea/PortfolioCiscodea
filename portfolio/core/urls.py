"""Core urls module"""

# Django
from django.urls import path

# Views
from .views import home

urlpatterns = [
    path(
        "",
        home,
        name="home"
    )
]