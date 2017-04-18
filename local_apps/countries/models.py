# -*- coding: utf-8 -*-
from django.db import models

class Country(models.Model):
    en_name = models.CharField(max_length=40)
    es_name = models.CharField(max_length=40)
    country_code = models.CharField(max_length=2)
    flag = models.ImageField(upload_to='countries/flags/')
    short_img = models.ImageField(
                                    upload_to='countries/short-images/',
                                    width_field="short_img_height",
                                    height_field="short_img_width",
                                    blank=True,
                                )
    short_img_height = models.IntegerField(default=0, blank=True,)
    short_img_width = models.IntegerField(default=0, blank=True,)
    large_img = models.ImageField(
                                    upload_to='countries/large-images/',
                                    width_field="large_img_height",
                                    height_field="large_img_width",
                                    blank=True,
                                )
    large_img_height = models.IntegerField(default=0, blank=True,)
    large_img_width = models.IntegerField(default=0, blank=True,)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.country_code

    class Meta:
        """# Class Meta"""
        verbose_name = ('Country')
        verbose_name_plural = ('countries')
