"""Main URLs module."""

# Django
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include(("portfolio.core.urls", "portfolio.core"), namespace="core"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
