# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import (
    path,
    re_path,
    include
)
from django.contrib import admin
from django.views.static import serve

from src.dashboard import views

app_name = 'dashboard'
urlpatterns = [
    # Frontend
    path('', views.dashboard_home, name='home'),
    # url(r'^', views.dashboard_home, name='home'),
]