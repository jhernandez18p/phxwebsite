# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField

from local_apps.countries.models import Country
from local_apps.frontend.models import Sub_category, Banner

class Category(models.Model):
    """# Category model class"""
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='brands/type/')
    short_image = models.ImageField(upload_to='brands/type/short/')
    large_image = models.ImageField(upload_to='brands/type/large/')

    def __str__(self):
        return self.en_name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Brand Category')
        verbose_name_plural = ('Brand Category')


class Type(models.Model):
    """# Type model class"""
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='brands/type/')
    short_image = models.ImageField(upload_to='brands/type/short/')
    large_image = models.ImageField(upload_to='brands/type/large/')
    sub_category = models.ForeignKey(
        Sub_category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '%s %s'%(self.en_name, self.sub_category)

    class Meta:
        """# Class Meta"""
        verbose_name = ('Brand Type')
        verbose_name_plural = ('Brand Type')


class Carousel(models.Model):
    """# Carousel model class"""
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ManyToManyField(Banner, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.en_name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Brand Carousel')
        verbose_name_plural = ('Brand Carousel')


class Brand(models.Model):
    """# Brand model class"""
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140)
    en_title = models.CharField(max_length=140)
    es_title = models.CharField(max_length=140)
    short_logo = models.ImageField(upload_to='brands/logos/short/')
    large_logo = models.ImageField(upload_to='brands/logos/large/')
    en_description = RichTextField()
    es_description = RichTextField()
    en_short_description = RichTextField()
    es_short_description = RichTextField()
    sub_category = models.ForeignKey(
        Sub_category,
        on_delete=models.CASCADE,
    )
    carousel_images = models.ManyToManyField(
        Banner,
        blank=True,
    )
    url = models.CharField(max_length=140, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    brand_type = models.ManyToManyField(Type, blank=True)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.en_name

    def get_absolute_url_en(self):
        """# Get absolute English URL """
        return reverse("en:brand_detail", kwargs={"id": self.id})

    def get_absolute_url_es(self):
        """# Get absolute Spanish URL """
        return reverse("es:brand_detail", kwargs={"id": self.id})


    class Meta:
        """# Class Meta"""
        verbose_name = ('Brand')
        verbose_name_plural = ('Brands')


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
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        blank=True
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        blank=True
    )
    google_iframe = models.CharField(max_length=220, blank=True)
    google_lat = models.CharField(max_length=220, blank=True)
    google_long = models.CharField(max_length=220, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.en_name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Location')
        verbose_name_plural = ('Locations')
