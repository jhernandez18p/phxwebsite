# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from local_apps.dashboard import views

urlpatterns = [
    # Frontend
    url(r'^', views.dashboard_home, name='home'),
    # url(r'^', views.dashboard_home, name='home'),
]