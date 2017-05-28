# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import (include, url, handler400, handler403, handler404, handler500)
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from local_apps.frontend import views as fw
from local_apps.profiles import auth as auth_views

handler400 = 'fw.my_custom_bad_request_view'
handler403 = 'fw.my_custom_permission_denied_view'
handler404 = 'fw.my_custom_page_not_found_view'
handler500 = 'fw.my_custom_error_view'

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
