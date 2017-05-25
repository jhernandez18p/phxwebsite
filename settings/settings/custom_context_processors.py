# -*- coding: utf-8 -*-
import random,datetime
from local_apps.blog.models import *
from local_apps.brands.models import *
from local_apps.countries.models import *
from local_apps.frontend.models import *
from local_apps.profiles.models import *

def menu(request):

    now = datetime.datetime.now()
    context = {
        'time':now,
    }
    newsletter_form = False
    context['newsletter_form'] = newsletter_form
    return context


def lang(request):

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

    # if lang_code == 'English':
    #     site_name = site.en_name
    # else:
    #     site_name = site.es_name

    context = {
        'lang_':lang_,
        'lang_code': lang_code,
        'lang':lang_code,
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