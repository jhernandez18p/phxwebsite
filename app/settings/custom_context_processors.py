# -*- coding: utf-8 -*-
import random
from datetime import datetime
from django.contrib.sessions.backends.db import SessionStore
from src.blog.models import *
from src.brands.models import *
from src.countries.models import *
from src.frontend.models import *
from src.profiles.models import *
from django.db import DEFAULT_DB_ALIAS

import json

def initial_data():
    pages = Pages.objects.all()
    if pages.exists():
        pass
        # for page in pages:
            # print(page.en_name)
    else:
        page_list = [
            {'es_name':"Inicio",'en_name':"Home"},
            {'es_name':"Quienes somos",'en_name':"About us"},
            {'es_name':"Marcas",'en_name':"Brands"},
            {'es_name':"Noticias",'en_name':"News"},
            {'es_name':"Contacto",'en_name':"Contact us"},
        ]

        for _object in page_list:
            # print(_object['en_name'])
            # print('------------')
            # print(_object['es_name'])
            Pages.objects.create(en_name=_object['en_name'], es_name=_object['es_name'])

    positions = Position.objects.all()
    if positions.exists():
        pass
        # for position in positions:
            # print(position)
    else:
        position_list = [
            {'en_name':'header','es_name':'header'},
            {'en_name':'section','es_name':'section'},
            {'en_name':'footer','es_name':'footer'},
            {'en_name':'full_screen','es_name':'full_screen'},
        ]

        for _object in position_list:
            # print(_object['en_name'])
            # print('----------------------')
            # print(_object['es_name'])
            Position.objects.create(en_name=_object['en_name'], es_name=_object['es_name'])
    
    companies = Company.objects.all().filter(is_default=True)
    if companies.exists():
        pass
        # for company in companies:
        #     print(company)
    else:
        Company.objects.create(
            es_name='Grupo PHX',
            en_name='Phoenix World Trade Inc.',
            en_title='Grupo PHX',
            es_title='Phoenix World Trade Inc.',
            es_description='Con más de 3.800 empleados, la compañía representa másde 40 de las mejores marcas internacionales en retail, más de 20 marcas en wholesale, más de 200 marcas en Travel Retail, apoyados en una sólida infraestructura, que supervisa más de 360 tiendas en 14 países, incluyendo Venezuela, Panamá, Colombia, Chile, Perú, Ecuador, Brasil,Costa Rica, República Dominicana, Aruba, St. Maarten, Puerto Rico, Curazao y EEUU. Desde 2011, Phoenix World Trade se embarca a su vez en bienes raíces, desarrollando proyectos immobiliarios tanto comerciales como residenciales.',
            en_description='With more than 3,800 employees, the company represents more than 40 of the best international brands in retail, more than 20 brands in wholesale, more than 200 brands in Travel Retail, supported by a solid infrastructure, which oversees more than 360 stores in 14 countries, Including Venezuela, Panama, Colombia, Chile, Peru, Ecuador, Brazil, Costa Rica, Dominican Republic, Aruba, St. Maarten, Puerto Rico, Curacao and USA. Since 2011, Phoenix World Trade has embarked on real estate, developing real estate projects both commercial and residential.',
            es_mision='Ofrecer a nuestros clientes la última tendencia de las mejores marcas del mundo.Crear marcas relevantes y representar firmas de primer nivel, llevando a nuestro mercado una experiencia de compra inolvidable en las mejores ubicaciones.',
            en_mision='To offer our customers the latest trend of the best brands in the world. Create relevant brands and represent top brands, leading to our market an unforgettable shopping experience in the best locations.',
            es_vision='Ser líderes de ventas al por menor en el mercado Latinoamericano.',
            en_vision='To be leaders of retail sales in the Latin American market.',
            default_lang=1,
            logo='',
            is_default=True,
        )

    brands = Brand.objects.all()
    if brands.exists():
        pass
        # for brand in brands:
            # print(brand)
    else:
        pass
        # brands_json = json.loads(open('app/dbs/brands.json').read())
        # for key,value in brands_json:
            # for objects in value:
        # print('----------------')
        # print(brands_json)
        # print('----------------')



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
    context = {}
    newsletter_form = False
    now = datetime.now()
    
    if request.META['HTTP_HOST'] == 'phoenixworldtrade.com':
        return_to_google = True
    else:
        return_to_google = False

    initial_data()

    context['time'] = now
    context['newsletter_form'] = newsletter_form
    context['return_to_google'] = return_to_google
    return context

def cookies(request):

    cookie = {}
    context = {} 

    try:
        site = Company.objects.all()
        # print(site.exists())
        if site.exists():
            cookie['en_name'] = site[0].en_name
            cookie['es_name'] = site[0].es_name
            cookie['en_mision'] = site[0].en_mision
            cookie['es_mision'] = site[0].es_mision
            cookie['en_vision'] = site[0].en_vision
            cookie['es_vision'] = site[0].es_vision
            cookie['en_name'] = site[0].en_name
            cookie['es_name'] = site[0].es_name
            cookie['logo'] = site[0].logo
            cookie['logo_sm'] = site[0].logo_sm
            cookie['logo_lg'] = site[0].logo_lg
            context['site'] = site[0]
        else:
            cookie['en_name'] = 'Phoenix World Trade Inc.'
            cookie['es_name'] = 'Grupo PHX'
            cookie['en_mision'] = 'To offer our customers the latest trend of the best brands in the world. Create relevant brands and represent top brands, leading to our market an unforgettable shopping experience in the best locations.'
            cookie['es_mision'] = 'Ofrecer a nuestros clientes la última tendencia de las mejores marcas del mundo.Crear marcas relevantes y representar firmas de primer nivel, llevando a nuestro mercado una experiencia de compra inolvidable en las mejores ubicaciones.'
            cookie['en_vision'] = 'To be leaders of retail sales in the Latin American market.'
            cookie['es_vision'] = 'Ser líderes de ventas al por menor en el mercado Latinoamericano.'
            cookie['logo'] = '/static/base/images/logo.png'
            cookie['logo_sm'] = '/static/base/images/logo.png'
            cookie['logo_lg'] = '/static/base/images/logo.png'

    except Exception as e:
        cookie['en_name'] = 'Phoenix World Trade Inc.'
        cookie['es_name'] = 'Grupo PHX'
        cookie['logo'] = '/static/base/images/logo.png'
        cookie['logo_sm'] = '/static/base/images/logo.png'
        cookie['logo_lg'] = '/static/base/images/logo.png'
        print('-------- Error custom context preprocessors -------')
        print(e)
        print('-------- Company error-------')


    if 'lang_' in request.COOKIES and 'lang_code' in request.COOKIES:
        lang_ = False
        lang_code = request.COOKIES['lang_code']
        if lang_code == 'English':
            site_name = cookie['en_name']
        else:
            site_name = cookie['es_name']
    else:
        lang_ = True
        site_name = cookie['en_name']
        lang_code = 'English'


    context['lang_'] = lang_ #cookie['lang'],
    context['lang_code'] = lang_code # cookie['language'],
    context['lang'] = lang_code # cookie['language'],
    context['site_name'] =site_name
    context['logo'] = cookie['logo']
    context['logo_sm'] = cookie['logo_sm']
    context['logo_lg'] = cookie['logo_lg']
    context['en_mision'] = cookie['en_mision']
    context['es_mision'] = cookie['es_mision']
    context['en_vision'] = cookie['en_vision']
    context['es_vision'] = cookie['es_vision']

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


    return context