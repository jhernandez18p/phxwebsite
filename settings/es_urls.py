# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from local_apps.frontend import views as fw 
from local_apps.profiles import auth as auth_views

urlpatterns = [
    url(r'^$', fw.index, name="es"),
    url(r'^quienes-somos/$', fw.history, name='historia'),
    url(r'^marcas/(?P<id>[\w-]+)/$', fw.brand_detail, name='brand_detail'),
    url(r'^marcas/$', fw.our_brands, name='marcas'),
    url(r'^noticias/$', fw.news, name='noticias'),
    url(r'^noticias/(?P<slug>[\w-]+)/$', fw.news_detail, name='detalle_noticias'),
    url(r'^contacto/$', fw.contact, name='contacto'),
]
