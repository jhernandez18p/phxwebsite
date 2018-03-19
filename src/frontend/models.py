# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template import defaultfilters
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from datetime import datetime
from ckeditor.fields import RichTextField

ICON_CHOICES = (
    ('home','home'),('sign-in','sign-in'),('sign-out','sign-out'),('user','user'),('users','users'),('lock','lock'),('unlock','unlock'),('settings','settings'),('cog','cog'),('nut','nut'),('comment','comment'),('commenting','commenting'),('comments','comments'),('hashtag','hashtag'),('tag','tag'),('cart','cart'),('credit-card','credit-card'),('mail','mail'),('search','search'),('location','location'),('bookmark','bookmark'),('code','code'),('paint-bucket','paint-bucket'),('camera','camera'),('bell','bell'),('bolt','bolt'),('star','star'),('heart','heart'),('happy','happy'),('lifesaver','lifesaver'),('rss','rss'),('social','social'),('git-branch','git-branch'),('git-fork','git-fork'),('world','world'),('calendar','calendar'),('clock','clock'),('history','history'),('future','future'),('pencil','pencil'),('trash','trash'),('move','move'),('link','link'),('question','question'),('info','info'),('warning','warning'),('image','image'),('thumbnails','thumbnails'),('table','table'),('list','list'),('menu','menu'),('grid','grid'),('more','more'),('more-vertical','more-vertical'),('plus','plus'),('plus-circle','plus-circle'),('minus','minus'),('minus-circle','minus-circle'),('close','close'),('check','check'),('ban','ban'),('refresh','refresh'),('play','play'),('play-circle','play-circle'),('Devices','Devices'),('tv','tv'),('desktop','desktop'),('laptop','laptop'),('tablet','tablet'),('phone','phone'),('tablet-landscape','tablet-landscape'),('phone-landscape','phone-landscape'),('Storage','Storage'),('file','file'),('copy','copy'),('file-edit','file-edit'),('folder','folder'),('album','album'),('push','push'),('pull','pull'),('server','server'),('database','database'),('cloud-upload','cloud-upload'),('cloud-download','cloud-download'),('download','download'),('upload','upload'),('Direction','Direction'),('reply','reply'),('forward','forward'),('expand','expand'),('shrink','shrink'),('arrow-up','arrow-up'),('arrow-down','arrow-down'),('arrow-left','arrow-left'),('arrow-right','arrow-right'),('chevron-up','chevron-up'),('chevron-down','chevron-down'),('chevron-left','chevron-left'),('chevron-right','chevron-right'),('triangle-up','triangle-up'),('triangle-down','triangle-down'),('triangle-left','triangle-left'),('triangle-right','triangle-right'),('Editor','Editor'),('bold','bold'),('italic','italic'),('strikethrough','strikethrough'),('video-camera','video-camera'),
)
SM_ICON_CHOICES = (
    (1,'behance'),(2,'dribbble'),(3,'facebook'),(4,'flickr'),(5,'foursquare'),(6,'github'),(7,'github-alt'),(8,'google'),(9,'google-plus'),(10,'instagram'),(11,'joomla'),(12,'linkedin'),(13,'pagekit'),(14,'pinterest'),(15,'soundcloud'),(16,'tripadvisor'),(17,'tumblr'),(18,'twitter'),(19,'uikit'),(20,'vimeo'),(21,'whatsapp'),(22,'wordpress'),(23,'xing'),(24,'yelp'),(25,'youtube'),
)


class Company(models.Model):
    """# Website model"""
    LANG_CHOICES = (
        (1,'en'),
        (2,'es'),
    )
    es_name = models.CharField(max_length=144,blank=True)
    en_name = models.CharField(max_length=144,blank=True)
    es_title = models.CharField(max_length=144,blank=True)
    en_title = models.CharField(max_length=144,blank=True)
    es_description = RichTextField(null=True,blank=True)
    en_description = RichTextField(null=True,blank=True)
    es_mision = RichTextField(null=True,blank=True)
    en_mision = RichTextField(null=True,blank=True)
    es_vision = RichTextField(null=True,blank=True)
    en_vision = RichTextField(null=True,blank=True)
    default_lang = models.PositiveSmallIntegerField(
        choices=LANG_CHOICES,
        null=True,
        blank=True
    )
    logo = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True, 
        width_field="width_field_logo", 
        height_field="height_field_logo"
    )
    logo_sm = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True, 
        width_field="width_field_logo_sm", 
        height_field="height_field_logo_sm"
    )
    logo_lg = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True, 
        width_field="width_field_logo_lg", 
        height_field="height_field_logo_lg"
    )
    mision_img = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True, 
        width_field="width_field_mision_img", 
        height_field="height_field_mision_img"
    )
    vision_img = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True, 
        width_field="width_field_vision_img", 
        height_field="height_field_vision_img"
    )
    timeline_img = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True, 
        width_field="width_field_timeline_img", 
        height_field="height_field_timeline_img"
    )
    width_field_logo = models.IntegerField(default=0, blank=True)
    height_field_logo = models.IntegerField(default=0, blank=True)
    width_field_logo_sm = models.IntegerField(default=0, blank=True)
    height_field_logo_sm = models.IntegerField(default=0, blank=True)
    width_field_logo_lg = models.IntegerField(default=0, blank=True)
    height_field_logo_lg = models.IntegerField(default=0, blank=True)
    width_field_mision_img = models.IntegerField(default=0, blank=True)
    height_field_mision_img = models.IntegerField(default=0, blank=True)
    width_field_vision_img = models.IntegerField(default=0, blank=True)
    height_field_vision_img = models.IntegerField(default=0, blank=True)
    width_field_timeline_img = models.IntegerField(default=0, blank=True)
    height_field_timeline_img = models.IntegerField(default=0, blank=True)
    # social_icons = models.ManyToManyField(Socialmedia, blank=True)
    # values = models.ManyToManyField(Site_value, blank=True)
    # country = models.ManyToManyField(Country, blank=True)
    is_default = models.BooleanField(default=False)


    def __str__(self):
        return self.es_name

    class Meta:
        verbose_name = _('Empresa')
        verbose_name_plural = _('Empresas')


class Pages(models.Model):

    en_name = models.CharField(max_length=144,blank=True)
    es_name = models.CharField(max_length=144,blank=True)
    en_desc = models.CharField(max_length=144,blank=True)
    es_desc = models.CharField(max_length=144,blank=True)
    es_title = models.CharField(max_length=144,blank=True)
    en_title = models.CharField(max_length=144,blank=True)
    es_url = models.CharField(max_length=144,blank=True)
    en_url = models.CharField(max_length=144,blank=True)
    
    def __str__(self):
        return self.es_name

    class Meta:
        verbose_name = _('Página')
        verbose_name_plural = _('Páginas')


class Position(models.Model):
    en_name = models.CharField(max_length=144, blank=True)
    es_name = models.CharField(max_length=144, blank=True)
    en_description = RichTextField(blank=True)
    es_description = RichTextField(blank=True)

    def __str__(self):
        return self.es_name

    class Meta:
        verbose_name = _('Posición')
        verbose_name_plural = _('Posiciones')


class Menu(models.Model):
    en_name = models.CharField(max_length=144, blank=True)
    es_name = models.CharField(max_length=144, blank=True)
    en_description = RichTextField(blank=True)
    es_description = RichTextField(blank=True)
    crated_at = models.DateTimeField(auto_now=True,)
    Position = models.OneToOneField(Position, related_name='position', on_delete=models.CASCADE,)
    Pages = models.ForeignKey(Pages, related_name='position', on_delete=models.CASCADE,)

    def __str__(self):
        return self.es_name

    class Meta:
        verbose_name = _('Menú')
        verbose_name_plural = _('Menú')


class Carousel(models.Model):
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)
    page = models.ForeignKey(Pages, default=1, on_delete=models.CASCADE,blank=True)
    Position = models.ForeignKey(Position, related_name="Page", on_delete=models.CASCADE,)
    crated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Carrusel")
        verbose_name_plural = _("Carrusel")


class CarouselImage(models.Model):
    Carousel = models.ForeignKey(Carousel, related_name='images', on_delete=models.CASCADE,)
    image = models.ImageField(upload_to="frontend/")
    name = models.CharField(max_length=144, blank=True)
    text = RichTextField(blank=True)
    call_to_action_url = models.CharField(
        max_length=144,
        blank=True
    )
    uploaded_at = models.DateTimeField(auto_now=True,)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Imágen del carousel")
        verbose_name_plural = _("Imagenes del carousel")


class Social(models.Model):

    name = models.CharField(max_length=144,blank=True)
    url = models.CharField(max_length=144,blank=True)
    icon = models.CharField(max_length=144,blank=True)
    icon = models.PositiveSmallIntegerField(
        choices=SM_ICON_CHOICES,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    Company = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE,
        default=1, 
        null=True
    )
        

    def __str__(self):
        return self.name

    class Meta:
        """# Class Meta"""
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Media')


class Country(models.Model):

    es_name = models.CharField(max_length=144, blank=True)
    en_name = models.CharField(max_length=144, blank=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=8, default=8.6571004)
    longitude = models.DecimalField(max_digits=19, decimal_places=8, default=-60.1603678)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.es_name

    class Meta:
        """# Class Meta"""
        verbose_name = _('País')
        verbose_name_plural = _('Países')



class Value(models.Model):
    
    en_name = models.CharField(max_length=144, blank=True)
    es_name = models.CharField(max_length=144, blank=True)
    en_description = RichTextField(blank=True)
    es_description = RichTextField(blank=True)
    icon = models.CharField(
            choices=ICON_CHOICES,
            null=True,
            blank=True,
            max_length=144
        )
    created_at = models.DateTimeField(auto_now_add=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.es_name

    class Meta:
        """# Class Meta"""
        verbose_name = _('Valores de la empresa')
        verbose_name_plural = _('Valores de la empresa')


class Timeline(models.Model):
    en_name = models.CharField(max_length=144,blank=True)
    es_name = models.CharField(max_length=144,blank=True)
    en_description = RichTextField(blank=True)
    es_description = RichTextField(blank=True)
    image = models.ImageField(
        upload_to='timeline', 
        default='/static/base/images/timeline_default.png',
        blank=True
    )
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(datetime.now().year-70), 
            MaxValueValidator(datetime.now().year)
        ],
        help_text="Use the following format: <YYYY>",
        blank=True
    )
    place = models.CharField(max_length=144,blank=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, default=1)


    def __str__(self):
        return self.es_name

    class Meta:
        """# Class Meta"""
        verbose_name = _('Linea de tiempo')
        verbose_name_plural = _('Linea de tiempo')
