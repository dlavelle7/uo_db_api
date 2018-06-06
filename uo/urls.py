from django.urls import path

from uo.health_view import health
from uo.users_view import Users

urlpatterns = [
    path('users', Users.as_view(), name='users'),
    path('health', health, name='health'),
]
