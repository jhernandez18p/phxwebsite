# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from django.contrib.flatpages import views as flats
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.static import serve

from src.frontend import views as fw
from src.profiles import auth as auth_views
from rest_framework import routers
from app.urls import rest

router = routers.DefaultRouter()
router.register(r'users', rest.UserViewSet)
router.register(r'groups', rest.GroupViewSet)

sitemaps = {
    'flatpages': FlatPageSitemap,
}

handler400 = 'app.urls.errors.bad_request_view'
handler403 = 'app.urls.errors.permission_denied_view'
handler404 = 'app.urls.errors.page_not_found_view'
handler500 = 'app.urls.errors.error_view'

app_name = 'base'
urlpatterns = [
    # Frontend
    path('', fw.home, name='home'),
    path('es/', include('app.urls.es_urls', namespace='es')),
    path('en/', include('app.urls.en_urls', namespace='en')),
    path('lang', fw.lang, name='lang'),
    path('subscribe', fw.subscribe, name='subscribe'),
    path('contact', fw.contact_post, name='contact_post'),
    # Auth
    path('login', auth_views.login, name = 'Login'),
    path('logout', auth_views.logout, name = 'Logout'),
    path('register', auth_views.register, name = 'Register'),
    # Backend
    path('dashboard', include('src.dashboard.urls', namespace='dashboard')),
    # Admin
    path('adminsite/', admin.site.urls),
    path('api', include(router.urls)),
    path('api/auth', include('rest_framework.urls', 
        namespace='rest_framework')),
    path('sitemap.xml', sitemap,{'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('<path:url>/', views.flatpage),
] 

if settings.DEBUG:
    urlpatterns += [
        re_path('^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

admin.site.site_header = 'CMS PHOENIX WORLD TRADE'
admin.site.site_title = 'CMS Phoenix World Trade'
