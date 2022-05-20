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
                  path('', mainView, name='main'),
                  path('tables/', tablesView, name='tables'),
                  path('queues/', queuesView, name='queues'),
                  path('teams/', teamsView, name='teams'),
                  path('shootersRank/', shootersRankView, name='shootersRank'),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('register/', registerView, name='register'),
                  path('login/', login_request, name='login'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
