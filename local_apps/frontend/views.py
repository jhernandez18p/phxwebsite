# -*- coding: utf-8 -*-
from django.core.mail import send_mail, BadHeaderError
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import *
import datetime
import random
import time

from local_apps.frontend.models import *
from local_apps.blog.models import *
from local_apps.brands.models import *
from local_apps.brands.models import Type as bt
from local_apps.brands.models import Category as bc
from local_apps.frontend.forms import *


def get_lang(request):
    if 'lang_code' in request.COOKIES:
        lang = request.COOKIES['lang_code']
    else:
        lang = 'English'
    return lang


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

        print(url)
        render = redirect(url)
        render.set_cookie('lang_code', lang_code)
        render.set_cookie('lang_', lang_)
        print(render)
        return render
    
    else:    
        print('La url del post es %s' % url)
        return redirect('en:en')


def home(request):

    template = 'frontend/index.html'
    
    if 'lang_code' in request.COOKIES:
        lang = request.COOKIES['lang_code']
        if lang == 'English':
            url = 'en:en'
            return redirect(url)
        else:
            url = 'es:es'
            return redirect(url)
    else:
        render = redirect('en:en')
        render.set_cookie('lang_code', 'English')
        render.set_cookie('lang_', False)
    context = {
        'pg_title':'home',
        'url':'home',
    }

    return render


def index(request):
    context = {
        'pg_title':'home',
        # 'profile':profile,
        # 'banners':banners,
        # 'contacts':locations,
    }
    template = 'frontend/index.html'

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
    
    
    context['url'] = url
    context['es_url'] = es_url
    context['title'] = title
    context['keywords'] = keywords
    sub_categories = Sub_category.objects.all()
    for sub_cat in sub_categories:
        if sub_cat.name == 'banner_top':
            banners_sub_cat = sub_cat
    #     if sub_cat.name == 'BUSINESS_CAROUSEL':
    #         business_sub_cat = sub_cat
    #     if sub_cat.name == 'PROFILE':
    #         profile_sub_cat = sub_cat
    #     if sub_cat.name == 'CONTACT':
    #         contact_sub_cat = sub_cat
        if sub_cat.name == 'news_blog':
            news_sub_cat = sub_cat
        if sub_cat.name == 'business_type':
            biz_sub_cat = sub_cat
    # print(news_sub_cat.id)
    # profile = get_object_or_404(Brand, sub_category=profile_sub_cat.id)
    banners = Banner.objects.all().filter(sub_category=banners_sub_cat.id)
    # banners_biz = Banner.objects.all().filter(sub_category=business_sub_cat.id)
    # print(banners)
    locations = Location.objects.all()
    news = Post.objects.all().filter(sub_category=news_sub_cat)[0:2]
    banners_biz = bt.objects.all()
    context['news'] = news
    context['banners_biz'] = banners_biz
    context['banners'] = banners

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

    try:
        brands_type = bt.objects.all()
        context['brands_type'] = brands_type
        brands_cat = bc.objects.all()
        context['brands_cat'] = brands_cat

        context['banners'] = brands_type  
    except Exception as e:
        raise e
    
    if request.method == "GET":
        if 'cat' in request.GET and 'type' in request.GET:
            brands = Brand.objects.all().filter(category=request.GET['cat'],brand_type=request.GET['type'])
        elif 'cat' in request.GET:
            try:
                brands = Brand.objects.all().filter(category=request.GET['cat'])
                context['brands'] = brands
            except Exception as e:
                print(e)
        elif 'type' in request.GET:
            try:
                brands = Brand.objects.all().filter(brand_type=request.GET['type'])
                context['brands'] = brands
            except Exception as e:
                print(e)
        else:

            brands = Brand.objects.all()
            context['brands'] = brands
        
    return render(request, template, context)


def news(request):
    template = 'frontend/news.html'
    context = {
        'pg_title':'news',
    }

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
    try:
        brands_cat = bt.objects.all()
        for x in brands_cat:
            if x.en_name == 'Retail':
                retail_cat = x
            elif x.en_name == 'Wholesale':
                wholesale_cat = x
        
        retail_brands = Brand.objects.all().filter(category=retail_cat.id)
        wholesale_brands = Brand.objects.all().filter(category=wholesale_cat.id)
        brands = Brand.objects.all()
        context['brands'] = brands
        context['brands_cat'] = brands_cat
        context['retail_cat'] = retail_cat  
        context['wholesale_cat'] = wholesale_cat    
        context['retail_brands'] = retail_brands    
        context['wholesale_brands'] = wholesale_brands  
        context['banners'] = brands_cat  
    except Exception as e:
        raise e

    try:
        news = Post.objects.all()
        context['news'] = news
    except Exception as e:
        raise e

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
    subscribers = Subscriber.objects.all()

    if request.method == "POST":
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
            return redirect(url)

    return render(request, template, context)


def contact_post(request):
    template = 'frontend/index.html'
    context = {}
    subscribers = Subscriber.objects.all()

    if request.method == "POST":
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
            return redirect(url)

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

def my_custom_bad_request_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '400'
    template = 'errors/400.html'
    return render(request, template, status=400)


def my_custom_permission_denied_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '403'
    template = 'errors/403.html'
    return render(request, template, status=403)


def my_custom_page_not_found_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '404'
    template = 'errors/404.html'
    return render(request, template, status=404)


def my_custom_error_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '500'
    template = 'errors/500.html'
    return render(request, template, status=500)