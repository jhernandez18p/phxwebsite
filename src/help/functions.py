# -*- coding: utf-8 -*-

def get_lang(request):
    if 'lang_code' in request.COOKIES:
        lang = request.COOKIES['lang_code']
    else:
        lang = 'English'
    return lang

def get_cookies(request):
    # 
    cookies = True
    return cookies