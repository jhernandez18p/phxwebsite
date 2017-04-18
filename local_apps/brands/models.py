# -*- coding: utf-8 -*-
from django.db import models
from local_apps.countries.models import Country
from local_apps.frontend.models import Sub_category

class Category(models.Model):
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='brands/type/')
    short_image = models.ImageField(upload_to='brands/type/short/')
    large_image = models.ImageField(upload_to='brands/type/large/')
    # background_color = models.ForeignKey(
    #     Color,
    #     on_delete=models.CASCADE,
    #     blank=True,
    # )

    def __str__(self):
        return self.en_name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Brand Category')
        verbose_name_plural = ('Brand Category')


class Type(models.Model):
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='brands/type/')
    short_image = models.ImageField(upload_to='brands/type/short/')
    large_image = models.ImageField(upload_to='brands/type/large/')
    # background_color = models.ForeignKey(
    #                                 Color,
    #                                 on_delete=models.CASCADE,
    #                                 blank=True,
    #                             )
    sub_category = models.ForeignKey(
                                    Sub_category,
                                    on_delete=models.CASCADE,
                                )

    def __str__(self):
        return '%s %s'%(self.en_name,self.sub_category)

    class Meta:
        """# Class Meta"""
        verbose_name = ('Brand Type')
        verbose_name_plural = ('Brand Type')


class Carousel(models.Model):
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='brands/carousel/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.en_name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Brand Carousel')
        verbose_name_plural = ('Brand Carousel')


class Brand(models.Model):
    en_name = models.CharField(max_length=140)
    es_name = models.CharField(max_length=140)
    en_title = models.CharField(max_length=140)
    es_title = models.CharField(max_length=140)
    short_logo = models.ImageField(upload_to='brands/logos/short/')
    large_logo = models.ImageField(upload_to='brands/logos/large/')
    # background_color = models.ForeignKey(
    #                                 Color,
    #                                 on_delete=models.CASCADE,
    #                                 blank=True,
    #                             )
    en_description = models.TextField()
    es_description = models.TextField()
    en_short_description = models.CharField(max_length=500, blank=True)
    es_short_description = models.CharField(max_length=500, blank=True)
    sub_category = models.ForeignKey(
                                    Sub_category,
                                    on_delete=models.CASCADE,
                                )
    carousel_images = models.ManyToManyField(Carousel, blank=True)
    url = models.CharField(max_length=140, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    brand_type = models.ManyToManyField(Type, blank=True)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.en_name

    def get_absolute_url_en(self):
        return reverse("en:brand_detail", kwargs={"id": self.id})

    def get_absolute_url_es(self):
        return reverse("es:brand_detail", kwargs={"id": self.id})


    class Meta:
        """# Class Meta"""
        verbose_name = ('Brand')
        verbose_name_plural = ('Brands')


class Location(models.Model):
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
                                )
    country = models.ForeignKey(
                                    Country,
                                    on_delete=models.CASCADE,
                                )
    google_iframe = models.CharField(max_length=220, blank=True)
    google_lat = models.CharField(max_length=220, blank=True)
    google_long = models.CharField(max_length=220, blank=True)
    short_map_image = models.ImageField(upload_to='brands/map/')
    large_map_image = models.ImageField(upload_to='brands/map/')
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
