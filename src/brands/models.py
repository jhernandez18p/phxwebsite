# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# from src.countries.models import Country
# from src.frontend.models import Widgets, Banner, Socialmedia


class BusinessModel(models.Model):
    """# Business model class"""
    en_name = models.CharField(max_length=140, verbose_name=_('Nombre español'))
    es_name = models.CharField(max_length=140, blank=True, verbose_name=_('Nombre inglés'))
    en_description = RichTextField(blank=True,verbose_name=_('Descripción'))
    es_description = RichTextField(blank=True,verbose_name=_('Description'))
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='brands/type/', blank=True,)
    short_image = models.ImageField(upload_to='brands/type/short/', blank=True, verbose_name=_('Imágen pequeña'))
    large_image = models.ImageField(upload_to='brands/type/large/', blank=True, verbose_name=_('Imágen grande'))


    def __str__(self):
        return self.es_name

    class Meta:
        """# Class Meta"""
        verbose_name = _('Segmento de negocio')
        verbose_name_plural = _('Segmentos de negocio')


class Department(models.Model):
    """# Category model class"""
    en_name = models.CharField(max_length=140, verbose_name=_('Nombre inglés'), blank=True)
    es_name = models.CharField(max_length=140, blank=True, verbose_name=_('Nombre español'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    image = models.ImageField(upload_to='brands/cat/', verbose_name=_('Imágem principal'), blank=True)
    short_image = models.ImageField(upload_to='brands/dep/short/', blank=True, verbose_name=_('Imágen pequeña'))
    large_image = models.ImageField(upload_to='brands/dep/large/', blank=True, verbose_name=_('Imágen grande'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    en_slug = models.CharField(max_length=140, blank=True, verbose_name=_('URL Slug español'))
    es_slug = models.CharField(max_length=140, blank=True, verbose_name=_('URL Slug inglés'))

    def get_absolute_url_en(self):
        """# Get absolute English URL """
        return reverse("en:brand_department", kwargs={"slug": self.en_slug})

    def get_absolute_url_es(self):
        """# Get absolute Spanish URL """
        return reverse("es:brand_department", kwargs={"slug": self.es_slug})

    def es_get_unique_slug(self):
        slug = slugify(self.es_name)
        unique_slug = slug
        num = int(self.id)
        while Brand.objects.filter(es_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, int(num))
            num += 1
        return unique_slug
    
    def en_get_unique_slug(self):
        slug = slugify(self.en_name)
        unique_slug = slug
        num = int(self.id)
        while Brand.objects.filter(en_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, int(num))
            num += 1
        return unique_slug

    def __str__(self):
        return self.es_name

    def save(self, *args, **kwargs):
        if self.es_slug == '':
            self.es_slug = self.es_get_unique_slug()
        if self.en_slug == '':
            self.en_slug = self.en_get_unique_slug()
        super().save()

    class Meta:
        """# Class Meta"""
        verbose_name = _('Departamento')
        verbose_name_plural = ('Departamentos')


class Category(models.Model):
    """# Category model class"""
    en_name = models.CharField(max_length=140, verbose_name=_('Nombre español'), blank=True)
    es_name = models.CharField(max_length=140, blank=True, verbose_name=_('Nombre inglés'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    image = models.ImageField(upload_to='brands/cat/', verbose_name=_('Imágen principal'), blank=True)
    short_image = models.ImageField(upload_to='brands/cat/short/', blank=True, verbose_name=_('Imágen pequeña'))
    large_image = models.ImageField(upload_to='brands/cat/large/', blank=True, verbose_name=_('Imágen grande'))

    def __str__(self):
        return self.es_name

    class Meta:
        """# Class Meta"""
        verbose_name = _('Categoría')
        verbose_name_plural = ('Categorias')


class Brand(models.Model):
    """# Brand model class"""


    def _get_upload_to(self, filename):
        upload_to = 'brands/%s/%s' % (self.es_slug,filename)
        return upload_to
        
    en_name = models.CharField(max_length=140, verbose_name=_('Nombre español'))
    es_name = models.CharField(max_length=140, verbose_name=_('Nombre inglés'))
    en_title = models.CharField(max_length=140, verbose_name=_('Titulo'))
    es_title = models.CharField(max_length=140, verbose_name=_('Title'))
    en_slug = models.CharField(max_length=140, blank=True, verbose_name=_('URL Slug español'))
    es_slug = models.CharField(max_length=140, blank=True, verbose_name=_('URL Slug inglés'))
    short_logo = models.ImageField(upload_to=_get_upload_to, verbose_name=_('Logo pequeño'))
    large_logo = models.ImageField(upload_to=_get_upload_to, verbose_name=_('Logo grande'))
    es_description = RichTextField(blank=True, verbose_name=_('Descripción español'))
    en_description = RichTextField(blank=True, verbose_name=_('Descripción ingles'))
    es_short_description = RichTextField(blank=True, verbose_name=_('Descripción corta español'))
    en_short_description = RichTextField(blank=True, verbose_name=_('Descripción corta inglés'))

    # carousel_images = models.ManyToManyField(verbose_name=_(''),
    #     Banner,
    #     blank=True,
    # )

    url = models.CharField(max_length=140, blank=True, verbose_name=_('Dirección url de la marca'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    brand_type = models.ManyToManyField(BusinessModel, blank=True,verbose_name=_('Modelo de negocio'))
    category = models.ManyToManyField(Category, blank=True,verbose_name=_('Categoría'))
    department = models.ManyToManyField(Department, blank=True,verbose_name=_('Departamentos'))
    featured = models.BooleanField(default=False, verbose_name=_('Marca destacada'))

    def __str__(self):
        return self.es_name

    def get_absolute_url_en(self):
        """# Get absolute English URL """
        return reverse("en:brand_detail", kwargs={"slug": self.en_slug})

    def get_absolute_url_es(self):
        """# Get absolute Spanish URL """
        return reverse("es:brand_detail", kwargs={"slug": self.es_slug})
    
    def es_get_unique_slug(self):
        slug = slugify(self.es_title)
        unique_slug = slug
        num = int(self.id)
        while Brand.objects.filter(es_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, int(num))
            num += 1
        return unique_slug
    
    def en_get_unique_slug(self):
        slug = slugify(self.en_title)
        unique_slug = slug
        num = int(self.id)
        while Brand.objects.filter(en_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, int(num))
            num += 1
        return unique_slug
    
    def save(self, *args, **kwargs):
        if self.es_slug == '':
            self.es_slug = self.es_get_unique_slug()
        if self.en_slug == '':
            self.en_slug = self.en_get_unique_slug()
        super().save()

    class Meta:
        """# Class Meta"""
        verbose_name = _('Marca')
        verbose_name_plural = ('Marcas')


class BrandImage(models.Model):
    Brand = models.ForeignKey(Brand, related_name='images', on_delete=models.CASCADE, verbose_name=_('Marca asociada'))
    image = models.ImageField(upload_to="frontend/", verbose_name=_('Imágen'))
    name = models.CharField(max_length=144, blank=True, verbose_name=_('Nombre español'))
    text = RichTextField(blank=True, verbose_name=_('Descripción'))
    call_to_action_url = models.CharField(verbose_name=_('Boton de enlace'),
        max_length=144,
        blank=True
    )
    uploaded_at = models.DateTimeField(auto_now=True, verbose_name=_('Ultima actualización'))
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Imágen del carousel")
        verbose_name_plural = _("Imagenes del carousel")


class Location(models.Model):
    """# Location model class"""
    en_name = models.CharField(max_length=140, verbose_name='Nombre español')
    es_name = models.CharField(max_length=140, verbose_name='Nombre inglés')
    es_description = models.TextField(blank=True, verbose_name=_('Descripción español'))
    en_description = models.TextField(blank=True, verbose_name=_('Descripción ingles'))
    es_short_description = models.CharField(max_length=500, blank=True, verbose_name=_('Descripción corta español'))
    en_short_description = models.CharField(max_length=500, blank=True, verbose_name=_('Descripción corta inglés'))
    email = models.CharField(max_length=140, blank=True, verbose_name=_('Correo electronico'))
    office_number = models.CharField(max_length=140, blank=True, verbose_name=_('Número de oficina'))
    phone_number = models.CharField(max_length=140, blank=True, verbose_name=_('Número de telefono'))
    google_iframe = models.CharField(max_length=220, blank=True, verbose_name=_('Enlace a iframe'))
    google_lat = models.DecimalField(verbose_name=_('Latitud'),
        max_digits=9, 
        decimal_places=6, 
        null=True, 
        blank=True
    )
    google_long = models.DecimalField(verbose_name=_('Longitud'),
        max_digits=9, 
        decimal_places=6, 
        null=True, 
        blank=True
    )
    instagram = models.CharField(max_length=50, blank=True, verbose_name=_('Instagram'))
    facebook = models.CharField(max_length=50, blank=True, verbose_name=_('Facebook'))
    twitter = models.CharField(max_length=50, blank=True, verbose_name=_('Twitter'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creada'))
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, verbose_name=_('Marca asociada'))

    def __str__(self):
        return self.es_name

    class Meta:
        """# Class Meta"""
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

