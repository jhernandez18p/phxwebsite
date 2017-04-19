from django.contrib import admin
from django.forms import SelectMultiple
from local_apps.brands.models import *

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    
    search_fields = ['es_name',]
    list_display = (
        'en_name',
        'es_name',
        'image',
        'short_image',
        'large_image',
        # 'background_color',
        'sub_category',
    )

    class Meta:
        model = Type


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'5', 'style': 'color:blue;width:250px'})},

    }
    search_fields = ['es_name',]
    list_display = (
                    'en_name',
                    'es_name',
                )

    class Meta:
        model = Type

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
        
    search_fields = ['es_name',]
    list_display = (
        'en_name',
        'es_name',
        'en_title',
        'es_title',
        'short_logo',
        'large_logo',
        # 'background_color',
        'en_description',
        'es_description',
        'en_short_description',
        'es_short_description',
        'sub_category',
        'url',
    )
    class Meta:
        model = Type


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
        
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
        'short_map_image',
        'large_map_image',
        'instagram',
        'facebook',
        'twitter',
    )
    class Meta:
        model = Type


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['es_name',]
    list_display = (
            'en_name',
        )

    class Meta:
        model = Type
