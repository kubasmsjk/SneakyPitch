from django.urls import path, include
from accounts.views import *

urlpatterns = [
    path('logout_user', logout_user, name='logout'),
    path('login_user', login_user, name='login'),
    path('register_user', register_user, name='register'),
    path('team_create', team_create, name='team_create'),
]
