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
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/', include('accounts.urls')),
<<<<<<< HEAD

=======
>>>>>>> c6bc06a117a85235b167be8f9a42765bfd07e4f1

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
