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
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140, blank=True)
    en_description = RichTextField(blank=True)
    es_description = RichTextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='brands/type/', blank=True)
    short_image = models.ImageField(upload_to='brands/type/short/', blank=True)
    large_image = models.ImageField(upload_to='brands/type/large/', blank=True)


    def __str__(self):
        return '%s %s'%(self.en_name, self.sub_category)

    class Meta:
        """# Class Meta"""
        verbose_name = _('Business Segment')
        verbose_name_plural = _('Business Segment')


class Brand(models.Model):
    """# Brand model class"""

    upload_to = 'brands/brand/%d/%s'

    def _get_upload_to(self, filename):
        return self.upload_to % (self.en_name, filename)

    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140)
    en_title = models.CharField(max_length=140)
    es_title = models.CharField(max_length=140)
    en_slug = models.CharField(max_length=140, blank=True)
    es_slug = models.CharField(max_length=140, blank=True)
    short_logo = models.ImageField(upload_to=_get_upload_to)
    large_logo = models.ImageField(upload_to=_get_upload_to)
    en_description = RichTextField()
    es_description = RichTextField()
    en_short_description = RichTextField()
    es_short_description = RichTextField()

    # carousel_images = models.ManyToManyField(
    #     Banner,
    #     blank=True,
    # )

    url = models.CharField(max_length=140, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    brand_type = models.ManyToManyField(BusinessModel, blank=True)

    def __str__(self):
        return self.en_name

    def get_absolute_url_en(self):
        """# Get absolute English URL """
        return reverse("en:brand_detail", kwargs={"id": self.id})

    def get_absolute_url_es(self):
        """# Get absolute Spanish URL """
        return reverse("es:brand_detail", kwargs={"id": self.id})
    
    def es_get_unique_slug(self):
        slug = slugify(self.es_title)
        unique_slug = slug
        num = 1
        while Brand.objects.filter(es_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    
    def en_get_unique_slug(self):
        slug = slugify(self.en_title)
        unique_slug = slug
        num = 1
        while Brand.objects.filter(en_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    
    def save(self, *args, **kwargs):
        if not self.es_slug:
            self.es_slug = self.es_get_unique_slug()
        if not self.en_slug:
            self.en_slug = self.en_get_unique_slug()
        super().save()

    class Meta:
        """# Class Meta"""
        verbose_name = _('Brand')
        verbose_name_plural = ('Brands')


class Department(models.Model):
    """# Category model class"""
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='brands/cat/')
    short_image = models.ImageField(upload_to='brands/cat/short/')
    large_image = models.ImageField(upload_to='brands/cat/large/')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)



class Category(models.Model):
    """# Category model class"""
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='brands/cat/')
    short_image = models.ImageField(upload_to='brands/cat/short/')
    large_image = models.ImageField(upload_to='brands/cat/large/')

    def __str__(self):
        return self.en_name

    class Meta:
        """# Class Meta"""
        verbose_name = _('Brand Category')
        verbose_name_plural = ('Brand Category')

class Location(models.Model):
    """# Location model class"""
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140)
    es_description = models.TextField(blank=True)
    en_description = models.TextField(blank=True)
    es_short_description = models.CharField(max_length=500, blank=True)
    en_short_description = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=140, blank=True)
    office_number = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=140, blank=True)
    google_iframe = models.CharField(max_length=220, blank=True)
    google_lat = models.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        null=True, 
        blank=True
    )
    google_long = models.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        null=True, 
        blank=True
    )
    instagram = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.en_name

    class Meta:
        """# Class Meta"""
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')


class BrandImage(models.Model):
    Brand = models.ForeignKey(Brand, related_name='images', on_delete=models.CASCADE,)
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