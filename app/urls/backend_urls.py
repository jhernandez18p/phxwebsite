# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from src.frontend import views as front_views
from src.profiles import auth as auth_views

urlpatterns = [
    # url(r'^$',front_views.dashboard_home, name='dashboard_home'),
]
