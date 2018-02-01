#-*- coding: utf-8 -*-
from django import forms

class LanguageForm(forms.Form):
   lang = forms.CharField(max_length = 5)
