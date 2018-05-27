from django.urls import path

from . import health_view

urlpatterns = [
    path('health', health_view.health, name='health'),
]
