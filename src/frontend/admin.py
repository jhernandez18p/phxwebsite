from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from src.frontend.models import (
    Company,  
    Position, 
    Menu, 
    Pages,
    Carousel, 
    CarouselImage,
    Social,
    Country,  
    Value,
    Timeline
)


class CompanySocialInline(admin.StackedInline):
    model = Social
    extra = 3
    verbose_name = _('Social media')
    verbose_name_plural = _('Social media')


class CompanyCountrylInline(admin.StackedInline):
    model = Country
    extra = 1
    verbose_name = _('Country')
    verbose_name_plural = _('Countries')


class CompanyValueInline(admin.StackedInline):
    model = Value
    extra = 1
    verbose_name = _('Value')
    verbose_name_plural = _('Values')


class CompanyTimelineInline(admin.StackedInline):
    model = Timeline
    extra = 1
    verbose_name = _('Timeline')
    verbose_name_plural = _('Timeline')


class PageMenuInline(admin.StackedInline):
    model = Menu
    extra = 1
    verbose_name = _('Menu')
    verbose_name_plural = _('Menu')


class CarouselImageInline(admin.StackedInline):
    model = CarouselImage
    extra = 1
    verbose_name = _('Carousel Image')
    verbose_name_plural = _('Carousel Image')


class CompanyAdmin(admin.ModelAdmin):
    inlines = [CompanySocialInline,CompanyCountrylInline,CompanyValueInline,CompanyTimelineInline]


class PagesAdmin(admin.ModelAdmin):
    inlines = [PageMenuInline,]


class CarouselAdmin(admin.ModelAdmin):
    inlines = [CarouselImageInline,]


admin.site.register(Company,CompanyAdmin)
admin.site.register(Carousel, CarouselAdmin)
# admin.site.register(Pages, PagesAdmin)
# admin.site.register(Position)
# admin.site.register(Timeline)
# admin.site.register(Country)
# admin.site.register(Value)
# admin.site.register(Menu)
# admin.site.register(Social)
# admin.site.register(CarouselImage)