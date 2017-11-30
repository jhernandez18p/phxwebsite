# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import (include, url, handler400, handler403, handler404, handler500)
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from local_apps.frontend import views as fw
from local_apps.profiles import auth as auth_views

handler400 = 'local_apps.frontend.my_custom_bad_request_view'
handler403 = 'local_apps.frontend.my_custom_permission_denied_view'
handler404 = 'local_apps.frontend.my_custom_page_not_found_view'
handler500 = 'local_apps.frontend.my_custom_error_view'

urlpatterns = [
    # Frontend
    url(r'^$', fw.home, name='home'),
    url(r'^es/', include('settings.es_urls', namespace='es')),
    url(r'^en/', include('settings.en_urls', namespace='en')),
    url(r'^lang/$', fw.lang, name='lang'),
    url(r'^subscribe/$', fw.subscribe, name='subscribe'),
    url(r'^contact/$', fw.contact_post, name='contact_post'),
    # Auth
    url(r'^login/$', auth_views.login, name = 'Login'),
    url(r'^logout/$', auth_views.logout, name = 'Logout'),
    url(r'^register/$', auth_views.login, name = 'Register'),
    # Backend
    url(r'^dashboard/', include('local_apps.dashboard.urls', namespace='dashboard')),
    url(r'^posts/',include('settings.backend_urls')),
    # Admin
    url(r'^adminsite/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns +=[
        url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT,}),
    ]
