# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from local_apps.frontend import views as fw
from local_apps.profiles import auth as auth_views

urlpatterns = [
    url(r'^$', fw.index, name="en" ),
    url(r'^about/$', fw.history, name='about'),
    url(r'^brands/(?P<id>[\w-]+)/$',fw.brand_detail,name='brand_detail'),
    url(r'^brands/$', fw.our_brands, name='our_brands'),
    url(r'^news/$', fw.news, name='news'),
    url(r'^news/(?P<slug>[\w-]+)/$', fw.news_detail, name='news_detail'),
    url(r'^contact/$', fw.contact, name='contact'),
    url(r'^search/$', fw.search, name='search'),
]
