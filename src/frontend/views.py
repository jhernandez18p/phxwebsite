# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import (send_mail, BadHeaderError)
from django.db.models import Q
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

    pages = Pages.objects.get(en_name="Home")
    if pages:
        position = Position.objects.get(en_name='full_screen')
        carrusel = Carousel.objects.filter(Q(page=pages.id) & Q(Position=position.id))
        # print(carrusel)
        if carrusel.exists():
            banners = CarouselImage.objects.filter(Carousel=carrusel[0].id)
            if banners.exists():
                context['full_banners'] = banners
            else:
                header_carousel = [
                    {'large_banner':'/static/base/images/banner-01.png','es_name':'banner 01','en_name':'banner 01'},
                    {'large_banner':'/static/base/images/banner-02.png','es_name':'banner 02','en_name':'banner 02'},
                    {'large_banner':'/static/base/images/banner-03.png','es_name':'banner 03','en_name':'banner 03'},
                ]
                context['full_banners'] = header_carousel

    home_brands = Brand.objects.all()
    if home_brands.exists():
        context['home_brands'] = home_brands[:52]
    
    companies = Company.objects.all()
    if companies.exists():
        context['companies'] = companies

    business_banners = BusinessModel.objects.all()
    if business_banners.exists():
        context['business_banners'] = business_banners

    news = Post.objects.all()[:6]
    if news.exists():
        context['news'] = news
    else:
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
            {
                'short_image':'',
                'en_name':'New blog post 04',
                'en_title':'New blog post 04',
                'en_short_description':'This is the news blog post number 01',
                'get_absolute_url_en':'#',
                'es_name':'Nueva publicacion 04',
                'es_title':'Nueva publicacion 04',
                'es_short_description':'este es el post numero 01',
                'get_absolute_url_es':'#',
            },
            {
                'short_image':'',
                'en_name':'New blog post 05',
                'en_title':'New blog post 05',
                'en_short_description':'This is the news blog post number 05',
                'get_absolute_url_en':'#',
                'es_name':'Nueva publicacion 05',
                'es_title':'Nueva publicacion 05',
                'es_short_description':'este es el post numero 02',
                'get_absolute_url_es':'#',
            },
            {
                'short_image':'',
                'en_name':'New blog post 06',
                'en_title':'New blog post 06',
                'en_short_description':'This is the news blog post number 06',
                'get_absolute_url_en':'#',
                'es_name':'Nueva publicacion 06',
                'es_title':'Nueva publicacion 06',
                'es_short_description':'este es el post numero 06',
                'get_absolute_url_es':'#',
            },
        ]
        context['news'] = news

    return render(request, template, context)

def history(request):
    context = {
        'pg_title':'about',
    }
    template = 'frontend/history.html'

    pages = Pages.objects.get(en_name='About us')
    if pages:
        position = Position.objects.get(en_name='header')
        carrusel = Carousel.objects.filter(Q(page=pages.id) & Q(Position=position.id))
        # print(carrusel)
        if carrusel.exists():
            banners = CarouselImage.objects.filter(Carousel=carrusel[0].id)
            if banners.exists():
                context['banners'] = banners

    lang = get_lang(request)
    url = 'en:about'
    es_url = 'es:historia'
    if lang == 'English':
        title = 'About'
        keywords = 'About'
    else:
        title = '¿Quienes somos?'
        keywords = '¿Quienes somos?'

    timeline = Timeline.objects.all()
    if timeline.exists():
        context['timeline'] = timeline
    context['url'] = url
    context['es_url'] = es_url
    context['title'] = title
    context['keywords'] = keywords
    context['history'] = True
    context['newsletter_form'] = True

    return render(request, template, context)

def our_brands(request):
    template = 'frontend/brands.html'
    context = {'pg_title':'our_brands',}
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

    department = Department.objects.all()
    if department.exists():
        context['brands_cat'] = department
    
    context['title'] = title    
    context['keywords'] = keywords

    brands = Brand.objects.filter(draft=False).order_by('en_name')
    if brands.exists():
        context['brands'] = brands
    
    # pages = Pages.objects.get(en_name='Brands')
    # if pages:
    #     position = Position.objects.get(en_name='header')
    #     carrusel = Carousel.objects.filter(Q(page=pages.id) & Q(Position=position.id))
    #     # print(carrusel)
    #     if carrusel.exists():
    #         banners = CarouselImage.objects.filter(Carousel=carrusel[0].id)
    #         if banners.exists():
    #             # context['banners'] = banners
    #             context['banners'] = banners
    #         else:
    #             news_banners = [
    #                 {
    #                     'large_image':'/static/base/images/retail.png',
    #                     'es_name':'Ventas al por menor',
    #                     'en_name':'Retail',
    #                     'es_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
    #                     'en_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
    #                 },
    #                 {
    #                     'large_image':'/static/base/images/wholesale.png',
    #                     'es_name':'Ventas al por mayor',
    #                     'en_name':'WHolesale',
    #                     'es_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
    #                     'en_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
    #                 },
    #                 {
    #                     'large_image':'/static/base/images/marketing.jpg',
    #                     'es_name':'Publicidad y Mercadeo',
    #                     'en_name':'Marketing & Advertising',
    #                     'es_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
    #                     'en_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
    #                 },
    #                 {
    #                     'large_image':'/static/base/images/travel.jpg',
    #                     'es_name':'Travel Retail',
    #                     'en_name':'Travel Retail',
    #                     'es_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
    #                     'en_description':'banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 banner 02 ',
    #                 },
    #             ]
    #             context['banners'] = news_banners
        
    return render(request, template, context)

def department_detail(request, slug):
    template = 'frontend/brands.html'
    context = {
        'pg_title':'our_brands',
    }
    current_department = get_object_or_404(Department,Q(en_slug=slug)|Q(es_slug=slug))

    brands = Brand.objects.filter(department__id=current_department.id).order_by('en_name')
    if brands.exists():
        context['brands_cat_detail'] = current_department
        context['brands'] = brands

    department = Department.objects.all()
    if department.exists():
        context['brands_cat'] = department

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

    news = Post.objects.all()
    if news.exists():
        context['news'] = news
    else:
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

    pages = Pages.objects.get(en_name='News')
    if pages:
        position = Position.objects.get(en_name='header')
        carrusel = Carousel.objects.filter(Q(page=pages.id) & Q(Position=position.id))
        # print(carrusel)
        if carrusel.exists():
            banners = CarouselImage.objects.filter(Carousel=carrusel[0].id)
            if banners.exists():
                # context['banners'] = banners
                context['news_banners'] = banners
            else:
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
        new = get_object_or_404(Post, es_slug=slug)
           
    else:
        new = get_object_or_404(Post, es_slug=slug)
        title = 'Nuestras marcas'
        keywords = 'Nuestras marcas'
    
    # print(new)
    if request.COOKIES['lang_code'] == 'English':
        context['title'] = new.en_title
        context['blog'] = '/es/noticias/%s/' % new.es_slug
        new = get_object_or_404(Post, en_slug=slug)
        context['obj'] = new
        print(context['blog'])
    else:
        context['title'] = new.es_title
        context['blog'] = '/en/news/%s/' % new.en_slug
        new = get_object_or_404(Post, es_slug=slug)
        context['obj'] = new
        print(context['blog'])

    return render(request, template, context)

def brand_detail(request, slug):
    template = 'detail/brand-detail.html'
    context = {}

    brand = get_object_or_404(Brand, Q(en_slug=slug) | Q(es_slug=slug) )
    context['brand'] = brand
    context['title'] = brand.es_name
    context['en_parent_url'] = reverse('en:our_brands') 
    context['es_parent_url'] = reverse('es:marcas')

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


