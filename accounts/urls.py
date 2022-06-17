from django.urls import path
from accounts.views import *

urlpatterns = [
    path('logout_user', logout_user, name='logout'),
    path('login_user', login_user, name='login'),
    path('register_user', register_user, name='register'),
    path('team_create', team_create, name='team-create'),
    path('players_add', players_add, name='players-add'),
    path('enter_results', enter_results, name='enter-results'),
    path('enter_results/<user>/', enter_results, name='enter-results'),
    path('enter_results/<user>/<id>/', enter_results, name='enter-results'),
    path('enter_results/<user>/<id>/<home_team>/', enter_results, name='enter-results'),
    path('enter_results/<user>/<id>/<home_team>/<away_team>/', enter_results, name='enter-results'),
]
