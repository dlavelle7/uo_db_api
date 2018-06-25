from django.urls import path

from uo.views import health
from uo.users_view import UsersView, UserView
from rest_framework.authtoken import views

urlpatterns = [
    path('users', UsersView.as_view(), name='users'),
    path('users/<pk>', UserView.as_view(), name='user'),
    path('api-token-auth', views.obtain_auth_token),
    path('health', health, name='health'),
]
