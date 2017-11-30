# -*- coding: utf-8 -*-
import random,datetime
from django.contrib.sessions.backends.db import SessionStore
from local_apps.blog.models import *
from local_apps.brands.models import *
from local_apps.countries.models import *
from local_apps.frontend.models import *
from local_apps.profiles.models import *


class language_cookies:

    def set_language(lang = True,lang_code = 'en'):
        # Creamos el idioma que se va a utizar en el sitio en diccionario
        # language_cookie = {
        #    'lang' : True/False,
        #    'lang_code' : en/es,
        #    'language' : English/Español,
        # }
        language = 'English' if lower(str(lang_code)) == 'en' else 'Español'

        language_cookie = {
            'lang' : lang,
            'lang_code' : lang_code,
            'language' : language,
        }

        cookie = SessionStore()
        cookie['lang'] = lang
        cookie['lang_code'] = lang_code
        cookie['language'] = language
        cookie.create()

        return language_cookie

    def exist(request):
        # Vamos a verificar si existe o no la cookie
        exist = True if request.session['lang'] else False
        return exist


def menu(request):

    now = datetime.datetime.now()
    context = {
        'time':now,
    }
    newsletter_form = False
    context['newsletter_form'] = newsletter_form
    if request.META['HTTP_HOST'] == 'phoenixworldtrade.com':# or request.META['HTTP_HOST'] == 'localhost:8000':
        return_to_google = True
    else:
        return_to_google = False
    context['return_to_google'] = return_to_google
    return context

def cookies(request):
    # 
    try:
        site = Site_info.objects.all().first()
        # if site.default_lang == 'en':
        #     site_name = site.en_name
        # else:
        #     site_name = site.es_name
    except Exception as e:
        raise e

    if 'lang_' in request.COOKIES and 'lang_code' in request.COOKIES:
        lang_ = False
        lang_code = request.COOKIES['lang_code']
    else:
        lang_ = True
        lang_code = 'English'

    # language_cookie_exist = language_cookies.exist(request)
    
    # if language_cookie_exist == False:
    #     cookie = language_cookies.set_language()
    # else:
    #     cookies = {}
    #     cookie['lang'] = request.session['lang']
    #     cookie['language'] = request.session['language']

    # if lang_code == 'English':
    #     site_name = site.en_name
    # else:
    #     site_name = site.es_name

    context = {
        'lang_': lang_, #cookie['lang'],
        'lang_code': lang_code, # cookie['language'],
        'lang': lang_code, # cookie['language'],
        # 'site_name':site_name,
        'cookie':request.COOKIES,
        'site':site,
    }

    try:
        if 'message' in request.COOKIES:
            message = request.COOKIES['message']
            context['message'] = message
            message_type = request.COOKIES['message_type'] 
            context['message_type'] = message_type
            message_title = request.COOKIES['message_title']
            context['message_title'] = message_title
            message_content = request.COOKIES['message_content']
            context['message_content'] = message_content
    except Exception as e:
        raise e

    # print(context)
    return context