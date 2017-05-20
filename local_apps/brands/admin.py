from django.contrib import admin
from django.db import models
from django.forms import SelectMultiple
from local_apps.brands.models import (
    Type,
    Carousel,
    Brand,
    Location,
    Category,
)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """# Type admin class"""
    search_fields = ['es_name',]
    list_display = (
        'en_name',
        'es_name',
        'image',
        'short_image',
        'large_image',
        'sub_category',
    )

    class Meta:
        """# Reference for model fields"""
        model = Type


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    """# Carousel admin class"""
    formfield_overrides = {
        models.ManyToManyField:{
            'widget': SelectMultiple(attrs={
                'size':'5', 'style': 'color:blue;width:250px'
                })
            },
    }
    search_fields = ['es_name',]
    list_display = (
        'en_name',
        'es_name',
    )

    class Meta:
        """# Reference for model fields"""
        model = Type

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """# Brand admin class"""
    search_fields = ['es_name',]
    list_display = (
        'en_name',
        'es_name',
        'en_title',
        'es_title',
        'short_logo',
        'large_logo',
        'en_description',
        'es_description',
        'en_short_description',
        'es_short_description',
        'sub_category',
        'url',
    )
    class Meta:
        """# Reference for model fields"""
        model = Type


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """# Location admin class"""
    search_fields = ['es_name',]
    list_display = (
        'en_name',
        'es_name',
        'brand',
        'es_description',
        'en_description',
        'es_short_description',
        'en_short_description',
        'email',
        'office_number',
        'phone_number',
        'country',
        'google_iframe',
        'google_lat',
        'google_long',
        'instagram',
        'facebook',
        'twitter',
    )
    class Meta:
        """# Reference for model fields"""
        model = Type


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """# Category admin class"""
    search_fields = ['es_name',]
    list_display = (
        'en_name',
    )

    class Meta:
        """# Reference for model fields"""
        model = Type
