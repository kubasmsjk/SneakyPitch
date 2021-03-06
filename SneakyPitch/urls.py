"""SneakyPitch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from GamePLAY.views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', main_view, name='main'),
                  path('tables/', tables_view, name='tables'),
                  path('queues/', queues_view, name='queues'),
                  path('teams/', teams_view, name='teams'),
                  path('shootersRank/', shooters_rank_view, name='shootersRank'),
                  path('teamStatistic/', team_statistic_view, name='team-statistic'),
                  path('playerStatistic/', player_statistic_view, name='player-statistic'),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('404/', custom_page_not_found_view, name='404'),
                  path('500/', custom_error_view, name='500'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'GamePLAY.views.custom_page_not_found_view'
handler500 = 'GamePLAY.views.custom_error_view'
