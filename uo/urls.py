from django.urls import path

from uo.health_view import health
from uo.users_view import Users
from rest_framework.authtoken import views

urlpatterns = [
    path('users', Users.as_view(), name='users'),
    path('api-token-auth', views.obtain_auth_token),
    path('health', health, name='health'),
]
