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

app_name = 'es'
urlpatterns = [
    path('', fw.index, name="es"),
    path('quienes-somos/', fw.history, name='historia'),
    path('marcas/<int:id>/', fw.brand_detail, name='brand_detail'),
    path('marcas/', fw.our_brands, name='marcas'),
    path('noticias/', fw.news, name='noticias'),
    path('noticias/<slug:slug>/', fw.news_detail, name='detalle_noticias'),
    path('contacto/', fw.contact, name='contacto'),
    path('contacto/gracias/', fw.contact, name='contacto_satisfactorio'),
    path('contacto/error/', fw.contact, name='contacto_error'),
    path('buscar/', fw.search, name='buscar'),
]
