# -*- coding: utf-8 -*-
from django.core.mail import (send_mail, BadHeaderError)
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import (Http404, HttpResponse, HttpResponseRedirect)
from django.shortcuts import (get_object_or_404, render, redirect)
from django.urls import reverse
from django.views.generic import *

import datetime
import random
import time

from src.frontend.models import *
from src.blog.models import *
from src.brands.models import *
from src.frontend.forms import *
from src.help.functions import (get_lang)

"""
Frontend Views
"""
def lang(request):
    if request.method == "POST":
        if 'url' in request.POST and 'lang_code' in request.POST:
            url = request.POST['url']
            lang_code = request.POST['lang_code']
            lang_ = False
        else:
            url = 'en:en'
            lang_code = 'English'
            lang_ = True

        if 'blog' in request.POST:
            blog = request.POST['blog']
            if blog != '':
                url = blog

        # print(url)
        render = redirect(url)
        render.set_cookie('lang_code', lang_code)
        render.set_cookie('lang_', lang_)
        # print(render)
        return render
    
    else:    
        print('La url del post es %s' % url)
        return redirect('en:en')

def home(request):
    """
    Redirect view
    """
    if 'lang_code' in request.COOKIES:
        lang = request.COOKIES['lang_code']
        if lang == 'English':
            lang = 'en'
        else:
            lang = 'es'
        url = '%s:%s' % (lang,lang)
        return redirect(url)
    else:
        render = redirect('en:en')
        render.set_cookie('lang_code', 'English')
        render.set_cookie('lang_', False)
        return render

def index(request):
    template = 'frontend/index.html'
    context = {}

    lang = get_lang(request)

    if lang == 'English':
        url = 'en:en'
        es_url = 'es:es'
        title = 'Home'
        keywords = 'Home'
    else:
        url = 'en:en'
        es_url = 'es:es'
        title = 'Inicio'
        keywords = 'Inicio'

    context['pg_title']= title
    context['url'] = url
    context['es_url'] = es_url
    context['title'] = title
    context['keywords'] = keywords

    pages = Pages.objects.all()
    if pages.exists():
        page = pages.filter(en_name="Home")
        # print(page[0].id)

    companies = Company.objects.all()
    if companies.exists():
        context['companies'] = companies
    
    positions = Position.objects.all()
    if positions.exists():
        header = positions.filter(en_name='header')
        footer = positions.filter(en_name='footer')
        section = positions.filter(en_name='section')
        full_screen = positions.filter(en_name='full_screen')

    header_carousel = [
        {'large_banner':'/static/base/images/banner-01.png','es_name':'banner 01','en_name':'banner 01'},
        {'large_banner':'/static/base/images/banner-02.png','es_name':'banner 02','en_name':'banner 02'},
        {'large_banner':'/static/base/images/banner-03.png','es_name':'banner 03','en_name':'banner 03'},
    ]

    business_banners = [
        {
            'image':'/static/base/images/retail.png',
            'es_name':'Ventas al por menor',
            'en_name':'Retail',
            'es_description':'El retail (también venta al detalle en español) es un sector económico que engloba a las empresas especializadas en la comercialización masiva de productos o servicios uniformes a grandes cantidades de clientes. Es el sector industrial que entrega productos al consumidor final.',
            'en_description':'Retail (also retail in Spanish) is an economic sector that includes companies specialized in mass marketing of products or services to large numbers of customers. It is the industrial sector that delivers products to the final consumer.',
        },
        {
            'image':'/static/base/images/wholesale.png',
            'es_name':'Ventas al por mayor',
            'en_name':'WHolesale',
            'es_description':'El mayor, venta de mayoreo, o distribuidor mayorista es un componente de la cadena de distribución, en que la empresa o el empresario no se pone en contacto directo con los consumidores o usuarios finales de sus productos, sino que entrega esta tarea a un especialista',
            'en_description':'The wholesale, wholesale, or wholesale distributor is a component of the distribution chain, in which the company or the employer does not get in direct contact with consumers or end users of their products, but delivers this task to a specialist',
        },
        {
            'image':'/static/base/images/marketing.jpg',
            'es_name':'Publicidad y Mercadeo',
            'en_name':'Marketing & Advertising',
            'es_description':'Una agencia de publicidad es una organización comercial independiente, compuesta de personas creativas y de negocios, que desarrolla, prepara y coloca la publicidad, por cuenta de un anunciante que busca encontrar consumidores para sus bienes y servicios o difundir sus ideas. Estas agencias están especializadas en la comunicación y ofrecen a sus clientes, de forma directa o subcontratada.',
            'en_description':'An advertising agency is an independent commercial organization, composed of creative and business people, that develops, prepares and places advertising, on behalf of an advertiser that seeks to find consumers for their goods and services or disseminate their ideas. These agencies are specialized in communication and offer their clients, directly or subcontracted.',
        },
        {
            'image':'/static/base/images/travel.jpg',
            'es_name':'Travel Retail',
            'en_name':'Travel Retail',
            'es_description':'Las tiendas libres de impuestos o, en inglés, duty-free shops son comercios al por menor que no aplican impuestos ni tasas locales o nacionales. Se encuentran a menudo en la zona internacional de los aeropuertos internacionales, puertos de mar o a bordo de las naves de pasajeros. No suele haber para viajeros por carretera o por tren, aunque varios pasos de frontera entre los Estados Unidos y Canadá tienen tiendas libres de impuestos para los viajeros por carretera.',
            'en_description':'Duty-free shops or, in English, duty-free shops are retail stores that do not charge taxes or local or national taxes. They are often found in the international zone of international airports, seaports or aboard passenger ships. It is not usually for travelers by road or train, although several border crossings between the United States and Canada have duty-free shops for road travelers.',
        },
    ]

    news = [
        {
            'short_image':'',
            'en_name':'New blog post 01',
            'en_title':'New blog post 01',
            'en_short_description':'This is the news blog post number 01',
            'get_absolute_url_en':'#',
            'es_name':'Nueva publicacion 01',
            'es_title':'Nueva publicacion 01',
            'es_short_description':'este es el post numero 01',
            'get_absolute_url_es':'#',
        },
        {
            'short_image':'',
            'en_name':'New blog post 02',
            'en_title':'New blog post 02',
            'en_short_description':'This is the news blog post number 02',
            'get_absolute_url_en':'#',
            'es_name':'Nueva publicacion 02',
            'es_title':'Nueva publicacion 02',
            'es_short_description':'este es el post numero 02',
            'get_absolute_url_es':'#',
        },
        {
            'short_image':'',
            'en_name':'New blog post 03',
            'en_title':'New blog post 03',
            'en_short_description':'This is the news blog post number 03',
            'get_absolute_url_en':'#',
            'es_name':'Nueva publicacion 03',
            'es_title':'Nueva publicacion 03',
            'es_short_description':'este es el post numero 03',
            'get_absolute_url_es':'#',
        },
    ]

    context['news'] = news
    context['business_banners'] = business_banners
    context['full_banners'] = header_carousel

    return render(request, template, context)

def history(request):
    context = {
        'pg_title':'about',
    }
    template = 'frontend/history.html'

    lang = get_lang(request)
    url = 'en:about'
    es_url = 'es:historia'
    if lang == 'English':
        title = 'About'
        keywords = 'About'
    else:
        title = '¿Quienes somos?'
        keywords = '¿Quienes somos?'

    banners = [
        {
            'short_banner':'/static/base/images/base.png',
            'es_name':'Banner 01',
            'en_name':'Banner 01',
        },
    ]

    timeline = Timeline.objects.all()
    if timeline.exists():
        context['timeline'] = timeline
    context['banners'] = banners
    context['url'] = url
    context['es_url'] = es_url
    context['title'] = title
    context['keywords'] = keywords
    context['history'] = True
    context['newsletter_form'] = True
    # sub_categories = Sub_category.objects.all()
    # for sub_cat in sub_categories:
    #     if sub_cat.name == 'ABOUT_HEADER_BANNER':
    #         banners_sub_cat = sub_cat

    # banners = Banner.objects.all().filter(sub_category=banners_sub_cat.id)[0]
    return render(request, template, context)

def our_brands(request):
    template = 'frontend/brands.html'
    context = {
        'pg_title':'our_brands',
    }
    lang = get_lang(request)
    url = 'en:our_brands'
    es_url = 'es:marcas'
    context['url'] = url
    context['es_url'] = es_url

    if lang == 'English':
        title = 'Our brands'
        keywords = 'Our brands'
    else:
        title = 'Nuestras marcas'
        keywords = 'Nuestras marcas'
    
    context['title'] = title    
    context['keywords'] = keywords

    # try:
    #     brands_type = Business.objects.all()
    #     context['brands_type'] = brands_type
    #     brands_cat = Category.objects.all()
    #     context['brands_cat'] = brands_cat

    #     context['banners'] = brands_type  
    # except Exception as e:
    #     raise e
    
    # if request.method == "GET":
    #     if 'cat' in request.GET and 'type' in request.GET:
    #         brands = Brand.objects.all().filter(category=request.GET['cat'],brand_type=request.GET['type'])
    #     elif 'cat' in request.GET:
    #         try:
    #             brands = Brand.objects.all().filter(category=request.GET['cat'])
    #             context['brands'] = brands
    #         except Exception as e:
    #             print(e)
    #     elif 'type' in request.GET:
    #         try:
    #             brands = Brand.objects.all().filter(brand_type=request.GET['type'])
    #             context['brands'] = brands
    #         except Exception as e:
    #             print(e)
    #     else:

    brands = Brand.objects.all()
    if brands.exists():
        context['brands'] = brands
        
    return render(request, template, context)

def news(request):
    template = 'frontend/news.html'
    context = {'pg_title':'news',}

    lang = get_lang(request)
    url = 'en:news'
    es_url = 'es:noticias'

    if lang == 'English':
        title = 'Last News'
        keywords = 'Last News'
    else:
        title = 'Últimas Noticias'
        keywords = 'Últimas Noticias'

    context['url'] = url
    context['es_url'] = es_url
    context['title'] = title
    context['keywords'] = keywords
    # try:
    #     brands_cat = Business.objects.all()
    #     for x in brands_cat:
    #         if x.en_name == 'Retail':
    #             retail_cat = x
    #         elif x.en_name == 'Wholesale':
    #             wholesale_cat = x
        
    #     retail_brands = Brand.objects.all().filter(category=retail_cat.id)
    #     wholesale_brands = Brand.objects.all().filter(category=wholesale_cat.id)
    #     brands = Brand.objects.all()
    #     context['brands'] = brands
    #     context['brands_cat'] = brands_cat
    #     context['retail_cat'] = retail_cat  
    #     context['wholesale_cat'] = wholesale_cat    
    #     context['retail_brands'] = retail_brands    
    #     context['wholesale_brands'] = wholesale_brands  
    #     context['banners'] = brands_cat  
    # except Exception as e:
    #     raise e

    # try:
    news = [
        {
            'short_image':'',
            'en_name':'New blog post 01',
            'en_title':'New blog post 01',
            'en_short_description':'This is the news blog post number 01',
            'get_absolute_url_en':'#',
            'es_name':'Nueva publicacion 01',
            'es_title':'Nueva publicacion 01',
            'es_short_description':'este es el post numero 01',
            'get_absolute_url_es':'#',
        },
        {
            'short_image':'',
            'en_name':'New blog post 02',
            'en_title':'New blog post 02',
            'en_short_description':'This is the news blog post number 02',
            'get_absolute_url_en':'#',
            'es_name':'Nueva publicacion 02',
            'es_title':'Nueva publicacion 02',
            'es_short_description':'este es el post numero 02',
            'get_absolute_url_es':'#',
        },
        {
            'short_image':'',
            'en_name':'New blog post 03',
            'en_title':'New blog post 03',
            'en_short_description':'This is the news blog post number 03',
            'get_absolute_url_en':'#',
            'es_name':'Nueva publicacion 03',
            'es_title':'Nueva publicacion 03',
            'es_short_description':'este es el post numero 03',
            'get_absolute_url_es':'#',
        },
    ]
    news_banners = [
        {
            'large_image':'/static/base/images/retail.png',
            'es_name':'Ventas al por menor',
            'en_name':'Retail',
            'es_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
            'en_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
        },
        {
            'large_image':'/static/base/images/wholesale.png',
            'es_name':'Ventas al por mayor',
            'en_name':'WHolesale',
            'es_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
            'en_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
        },
        {
            'large_image':'/static/base/images/marketing.jpg',
            'es_name':'Publicidad y Mercadeo',
            'en_name':'Marketing & Advertising',
            'es_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
            'en_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
        },
        {
            'large_image':'/static/base/images/travel.jpg',
            'es_name':'Travel Retail',
            'en_name':'Travel Retail',
            'es_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
            'en_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
        },
    ]

    context['news_banners'] = news_banners
    context['news'] = news
    # except Exception as e:
    #     raise e

    return render(request, template, context)

def contact(request):

    template = 'frontend/contact.html'
    context = {
        'pg_title':'contact',
    }
    lang = get_lang(request)
    url = 'en:contact'
    es_url = 'es:contacto'

    if lang == 'English':
        title = 'Contact us'
        keywords = 'Contact us'
    else:
        title = 'Contactenos'
        keywords = 'Contactenos'

    context['url'] = url
    context['es_url'] = es_url
    context['title'] = title
    context['keywords'] = keywords
    context['newsletter_form'] = True
    
    if request.method == 'POST':
        name  = request.POST.get('name','')
        surname = request.POST.get('surname','')
        email = request.POST.get('email','')
        url = request.POST.get('url','')
        _file = request.POST.get('_file','')
        name = request.POST.get('name','')
        category = request.POST.get('category','')
        subject = request.POST.get('subject','')
        comments = request.POST.get('comments','')
        radio1 = request.POST.get('radio1','')
        radio2 = request.POST.get('radio2','')
        radio3 = request.POST.get('radio3','')
        message = request.POST.get('message','')
        print(
            name, '-',
            surname, '-',
            email, '-',
            url, '-',
            _file, '-',
            name, '-',
            category, '-',
            subject, '-',
            comments, '-',
            radio1, '-',
            radio2, '-',
            radio3, '-',
            message, '-',
        )
        pass

    elif request.method == 'GET':
        print('Get')
    else:
        print('None')

    return render(request, template, context)

def news_detail(request, slug):
    template = 'detail/news.html'
    context = {
        'pg_title':'news',
    }
    lang = get_lang(request)
    url = 'en:news'
    es_url = 'es:noticias'
    context['url'] = url
    context['es_url'] = es_url

    if lang == 'English':
        title = 'Our brands'
        keywords = 'Our brands'
        try:
            new = get_object_or_404(Post, en_slug=slug)
        except Exception as e:
            raise e
    else:
        try:
            new = get_object_or_404(Post, es_slug=slug)
        except Exception as e:
            raise e
        title = 'Nuestras marcas'
        keywords = 'Nuestras marcas'
    
    # print(new)
    context['obj'] = new
    if request.COOKIES['lang_code'] == 'English':
        context['title'] = new.en_title
        context['blog'] = '/es/noticias/%s/' % new.es_slug
        print(context['blog'])
    else:
        context['title'] = new.es_title
        context['blog'] = '/en/news/%s/' % new.en_slug
        print(context['blog'])

    return render(request, template, context)

def brand_detail(request, id):
    template = 'detail/news.html'
    context = {}

    try:
        new = get_object_or_404(Post, id=id)
        context['new'] = new
        print(context)
    except Exception as e:
        raise e

    return render(request, template, context)

def subscribe(request):
    template = 'frontend/index.html'
    context = {}

    if request.method == "POST":
        subscribers = Subscriber.objects.all()
        
        if 'email' in request.POST:

            email = request.POST['email']
            url =  request.POST['url']
            lang = request.COOKIES['lang_code']
            subscribed = False

            for x in subscribers:
                if email == x.email:
                    subscribed = True

            if subscribed:
                if lang == 'English':

                    message_title = 'Ups!. You have already subscribed'
                    message_content = 'Sorry %s, You have already subscribed'%(email)
                    message_type = 'warning'
                else:

                    message_title = 'Ups!. Ya estas subscrito'
                    message_content = 'Disculpe %s, Usted ya está suscrito'%(email)
                    message_type = 'warning'
            else:

                if lang == 'English':

                    message_title = 'Congratulations!'
                    message_content = 'Thanks %s, You are already subscribed'%(email)
                    message_type = 'success'

                else:

                    message_title = 'enhorabuena!'
                    message_content = 'Gracias %s, Usted se ha suscrito correctamente'%(email)
                    message_type = 'success'

                new = Subscriber.objects.create(email=email)
            
            render = redirect(url)
            render.set_cookie('message', True, max_age=20)
            render.set_cookie('message_type', message_type)
            render.set_cookie('message_title', message_title)
            render.set_cookie('message_content', message_content)
            return render
    else:

        lang = request.COOKIES['lang_code']
        if lang == 'English':
            url = 'en'
            return redirect(url)
        else:
            url = 'es'

        render = redirect('%s:%s' %(url,url))
        return render

    return render(request, template, context)

def contact_post(request):
    template = 'frontend/index.html'
    context = {}

    if request.method == "POST":
        subscribers = Subscriber.objects.all()
        if 'email' in request.POST:
            email = request.POST['email']
            url =  request.POST['url']
            lang = request.COOKIES['lang_code']
        if 'name' in request.POST:
            _name = request.POST['name']
        if 'surname' in request.POST:
            _surname = request.POST['name']
        if 'category' in request.POST:
            _category = request.POST['name']
        if 'subject' in request.POST:
            _subject = request.POST['name']
        if 'comments' in request.POST:
            _comments = request.POST['name']
        if 'radio1' in request.POST:
            _radio1 = request.POST['name']
        if 'type' in request.POST:
            _type = request.POST['name']
        if 'radio1' in request.POST:
            _radio1 = request.POST['name']


            if email != '':
                subscribed = True


            if subscribed:
                if lang == 'English':
                    message_title = 'Ups!. You have already subscribed'
                    message_content = 'Sorry %s, You have already subscribed'%(email)
                    message_type = 'warning'
                else:
                    message_title = 'Ups!. Ya estas subscrito'
                    message_content = 'Disculpe %s, Usted ya está suscrito'%(email)
                    message_type = 'warning'
            else:
                if lang == 'English':
                    message_title = 'Congratulations!'
                    message_content = 'Thanks %s, You are already subscribed'%(email)
                    message_type = 'success'
                else:
                    message_title = 'enhorabuena!'
                    message_content = 'Gracias %s, Usted se ha suscrito correctamente'%(email)
                    message_type = 'success'
                new = Subscriber.objects.create(email=email)
            
            render = redirect(url)
            render.set_cookie('message', True, max_age=20)
            render.set_cookie('message_type', message_type)
            render.set_cookie('message_title', message_title)
            render.set_cookie('message_content', message_content)
            return render
    else:

        lang = request.COOKIES['lang_code']
        if lang == 'English':
            url = 'en'
            return redirect(url)
        else:
            url = 'es'

        render = redirect('%s:%s' %(url,url))
        return render

    return render(request, template, context)

def search(request):
    template = 'frontend/search.html'
    context = {
        'pg_title':'search',
        'url':'en:search',
        'es_url':'es:buscar',
    }
    lang = get_lang(request)


    if lang == 'English':
        title = 'Search'
        keywords = 'Search...'
    else:
        title = 'Buscar'
        keywords = 'Buscar...'
    
    context['title'] = title

    if request.method == 'POST':

        if 'search' in request.POST:
            keyword = request.POST['search']
            brands = Brand.objects.all().filter(en_slug=keyword)
            print(brands)

        elif 'buscar' in request.POST:
            keyword = request.POST['buscar']
            brands = Brand.objects.all().filter(es_slug=keyword)
            print(brands)

        if len(brands)>=1:
            context['brands'] = brands
            context['brands_len'] = len(brands)
            context['searches'] = True

    return render(request,template,context)


