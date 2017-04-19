from django.contrib import admin

from local_apps.frontend.models import (
        Timeline,
        Site_info,
        Category,
        Sub_category,
        Banner,
        # Color,
        Subscriber,
        Socialmedia,
        Site_value,
    )

@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    search_fields = ['es_name',]
    list_display = (
                    'es_name',
                )
    class Meta:
        model = Timeline


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = (
                    'name',
                )
    class Meta:
        model = Category


@admin.register(Sub_category)
class Sub_categoryAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = (
                    'category',
                    'name',
                )
    class Meta:
        model = Sub_category


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    search_fields = ['es_name',]
    list_display = (
                    'en_name',
                    'es_name',
                    'short_banner',
                    'short_banner_height',
                    'short_banner_width',
                    'large_banner',
                    'large_banner_height',
                    'large_banner_width',
                    'sub_category',
                )

    class Meta:
        model = Banner


# @admin.register(Color)
# class ColorAdmin(admin.ModelAdmin):
#     search_fields = ['name',]
#     list_display = (
#                     'name',
#                 )

#     class Meta:
#         model = Color


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    search_fields = ['email',]
    list_display = (
                    'email',
                )

    class Meta:
        model = Subscriber


@admin.register(Socialmedia)
class SocialmediaAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = (
                    'name',
                )

    class Meta:
        model = Socialmedia


@admin.register(Site_value)
class Site_valueAdmin(admin.ModelAdmin):
    search_fields = ['es_name',]
    list_display = (
                    'es_name',
                )

    class Meta:
        model = Site_value


@admin.register(Site_info)
class SiteAdmin(admin.ModelAdmin):

    search_fields = ['en_name','es_name']
    list_display = (
                    'en_name',
                    'es_name',
                )

    class Meta: 
        model = Site_info