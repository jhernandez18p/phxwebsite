# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import (
    path,
    re_path,
    include
)
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from src.frontend import views as fw
from src.profiles import auth as auth_views

# handler400 = 'app.urls.errors.my_custom_bad_request_view'
# handler403 = 'app.urls.errors.my_custom_permission_denied_view'
# handler404 = 'app.urls.errors.my_custom_page_not_found_view'
# handler500 = 'app.urls.errors.my_custom_error_view'

app_name = 'en'
urlpatterns = [
    path('', fw.index, name="en" ),
    path('about', fw.history, name='about'),
    path('brands/<slug>',fw.brand_detail,name='brand_detail'),
    path('brands', fw.our_brands, name='our_brands'),
    path('news', fw.news, name='news'),
    path('news/<slug:slug>', fw.news_detail, name='news_detail'),
    path('contact', fw.contact, name='contact'),
    path('contact/thanks', fw.contact, name='contact_success'),
    path('contact/error', fw.contact, name='contact_error'),
    path('search', fw.search, name='search'),
]
