from django.conf import settings
from django.contrib import admin
from django.db import models
from django.forms import SelectMultiple

from src.brands.models import (
    BusinessModel,
    Brand,
    Department,
    Category,
    Location,
    BrandImage,
)

class BrandAdmin(admin.ModelAdmin):
    list_display = [ "es_slug","es_name","en_name","es_title","en_title"]
    list_display_links = ["es_slug",]
    list_editable = ["es_name"]
    list_filter = ["department"]
    search_fields = ["es_name","en_name","es_title","en_title"]

admin.site.register(BusinessModel)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(BrandImage)

# @admin.register(Business)
# class BusinessAdmin(admin.ModelAdmin):
#     """# Type admin class"""
#     search_fields = ['es_name',]
#     # list_display = (
#     #     'en_name',
#     #     'es_name',
#     #     'image',
#     #     'short_image',
#     #     'large_image',
#     #     'sub_category',
#     # )

#     class Meta:
#         """# Reference for model fields"""
#         model = Business


# @admin.register(Carousel)
# class CarouselAdmin(admin.ModelAdmin):
#     """# Carousel admin class"""
#     formfield_overrides = {
#         models.ManyToManyField:{
#             'widget': SelectMultiple(attrs={
#                 'size':'5', 'style': 'color:blue;width:250px'
#                 })
#             },
#     }
#     search_fields = ['es_name',]
#     list_display = (
#         'en_name',
#         'es_name',
#     )

#     class Meta:
#         """# Reference for model fields"""
#         model = Carousel

# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     """# Brand admin class"""
#     search_fields = ['es_name',]
#     list_display = (
#         'en_name',
#         'es_name',
#         'en_title',
#         'es_title',
#         'short_logo',
#         'large_logo',
#         'en_description',
#         'es_description',
#         'en_short_description',
#         'es_short_description',
#         'sub_category',
#         'url',
#     )
#     class Meta:
#         """# Reference for model fields"""
#         model = Brand


# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     """# Location admin class"""
#     search_fields = ['es_name',]
#     list_display = (
#         'en_name',
#         'es_name',
#         'brand',
#         'es_description',
#         'en_description',
#         'es_short_description',
#         'en_short_description',
#         'email',
#         'office_number',
#         'phone_number',
#         # 'country',
#         'google_iframe',
#         'google_lat',
#         'google_long',
#         'instagram',
#         'facebook',
#         'twitter',
#     )


#     class Media:
#         # if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
#         css = {
#             'all': ('%s/base/css/location_picker.css' % (settings.STATICFILES_DIRS),),
#         }
#         js = (
#             'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
#             '%s/base/js/location_picker.js' % (settings.STATICFILES_DIRS),
#         )

#     class Meta:
#         """# Reference for model fields"""
#         model = Location


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     """# Category admin class"""
#     search_fields = ['es_name',]
#     list_display = (
#         'en_name',
#     )

#     class Meta:
#         """# Reference for model fields"""
#         model = Category
