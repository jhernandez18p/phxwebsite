# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from local_apps.frontend import views as front_views
from local_apps.profiles import auth as auth_views

urlpatterns = [
    url(r'^$', front_views.index, name="en" ),
    url(r'^about/$', front_views.history, name='about'),
    url(
            r'^brands/(?P<id>[\w-]+)/$', 
            front_views.news_detail, 
            name='brand_detail'
        ),
    url(r'^brands/$', front_views.our_brands, name='our_brands'),
    url(r'^news/$', front_views.news, name='news'),
    url(r'^news/(?P<slug>[\w-]+)/$', front_views.news_detail, name='news_detail'),
    url(r'^contact/$', front_views.contact, name='contact'),
]
