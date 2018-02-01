# -*- coding: utf-8 -*-
from django.core.mail import send_mail, BadHeaderError
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import *
import datetime
import random
import time

# Create your views here.
def home(request):
	if request.method == "POST":
		context = {
		'pg_title':'',
		'url':'',
		'es_url':'o',
		}
	
		template = 'auth/login.html'

		return render(request, template, context)
	else:
		return render(request, 'auth/login.html',{'title':'Iniciar Sesión'})
	

def dashboard_redirect(request):
    url = 'Login'
    render = HttpResponseRedirect(reverse(url))
    return render


@login_required(login_url='/login/')
def dashboard_home(request):
	
	context = {
	    'pg_title':'dashboard',
	    # 'title':'Inicio',
	    'url':'dashboard:home',
	}

	user = request.user

	if user.is_authenticated:
		context['title'] = 'Inicio'
		template = 'dashboard/index.html'
	else:
		context['title'] = 'Iniciar sesión'
		template = 'auth/login.html'

	return render(request, template, context)
