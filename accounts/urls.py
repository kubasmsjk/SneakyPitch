from django.urls import path
from accounts.views import *

urlpatterns = [
    path('logout_user', logout_user, name='logout'),
    path('login_user', login_user, name='login'),
    path('register_user', register_user, name='register'),
    path('team_create', team_create, name='team-create'),
    path('players_add', players_add, name='players-add'),
    path('enter_results/<str:user>/<str:id>/<str:home_team>/<str:away_team>/', enter_results, name='enter-results'),
]
