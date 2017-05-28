from django.db import models
from ckeditor.fields import RichTextField
from django.template import defaultfilters
import datetime


class Timeline(models.Model):
    es_name = models.CharField(max_length=144)
    en_name = models.CharField(max_length=144)
    year = models.PositiveSmallIntegerField(blank=True)
    es_place = models.CharField(max_length=144)
    en_place = models.CharField(max_length=144)
    es_description = RichTextField()
    en_description = RichTextField()

    def __str__(self):
        return str(self.year)

    class Meta:
        """# Class Meta"""
        verbose_name = ('Timeline')
        verbose_name_plural = ('Timeline')
        ordering = ["-year"]


class Country(models.Model):
    es_name = models.CharField(max_length=144)
    en_name = models.CharField(max_length=144)
    latitude = models.DecimalField(max_digits=19, decimal_places=8, default=8.6571004)
    longitude = models.DecimalField(max_digits=19, decimal_places=8, default=-60.1603678)

    def __str__(self):
        return self.en_name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Country')
        verbose_name_plural = ('Countries')

class Category(models.Model):
    name = models.CharField(max_length=144)

    def __str__(self):
        return self.name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')


class Sub_category(models.Model):
    category = models.ForeignKey(
                                    Category,
                                    on_delete=models.CASCADE,
                                )
    name = models.CharField(max_length=144)

    def __str__(self):
        return self.name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Sub category')
        verbose_name_plural = ('Sub categories')


class Banner(models.Model):
    en_name = models.CharField(max_length=144)
    es_name = models.CharField(max_length=144)
    short_banner = models.ImageField(
                                    upload_to='banners/short/',
                                    width_field="short_banner_height",
                                    height_field="short_banner_width",
                                    blank=True,
                                )
    short_banner_height = models.IntegerField(default=0, blank=True,)
    short_banner_width = models.IntegerField(default=0, blank=True,)
    large_banner = models.ImageField(
                                    upload_to='banners/large/',
                                    width_field="large_banner_height",
                                    height_field="large_banner_width",
                                    blank=True,
                                )
    large_banner_height = models.IntegerField(default=0, blank=True,)
    large_banner_width = models.IntegerField(default=0, blank=True,)
    sub_category = models.ForeignKey(
                                    Sub_category,
                                    on_delete=models.CASCADE,
                                )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.en_name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Banner')
        verbose_name_plural = ('Banners')


class Subscriber(models.Model):
    email = models.CharField(max_length=144)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        """# Class Meta"""
        verbose_name = ('Subscriber')
        verbose_name_plural = ('Subscribers')


class Socialmedia(models.Model):
    SM_ICON_CHOICES = (
            (1,'behance'),
            (2,'dribbble'),
            (3,'facebook'),
            (4,'flickr'),
            (5,'foursquare'),
            (6,'github'),
            (7,'github-alt'),
            (8,'google'),
            (9,'google-plus'),
            (10,'instagram'),
            (11,'joomla'),
            (12,'linkedin'),
            (13,'pagekit'),
            (14,'pinterest'),
            (15,'soundcloud'),
            (16,'tripadvisor'),
            (17,'tumblr'),
            (18,'twitter'),
            (19,'uikit'),
            (20,'vimeo'),
            (21,'whatsapp'),
            (22,'wordpress'),
            (23,'xing'),
            (24,'yelp'),
            (25,'youtube'),
        )
    name = models.CharField(max_length=144)
    url = models.CharField(max_length=144, default="#")
    icon = models.PositiveSmallIntegerField(
            choices=SM_ICON_CHOICES,
            null=True,
            blank=True
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Social Media')
        verbose_name_plural = ('Social Media')


class Site_value(models.Model):
    ICON_CHOICES = (
            ('home','home'),
            ('sign-in','sign-in'),
            ('sign-out','sign-out'),
            ('user','user'),
            ('users','users'),
            ('lock','lock'),
            ('unlock','unlock'),
            ('settings','settings'),
            ('cog','cog'),
            ('nut','nut'),
            ('comment','comment'),
            ('commenting','commenting'),
            ('comments','comments'),
            ('hashtag','hashtag'),
            ('tag','tag'),
            ('cart','cart'),
            ('credit-card','credit-card'),
            ('mail','mail'),
            ('search','search'),
            ('location','location'),
            ('bookmark','bookmark'),
            ('code','code'),
            ('paint-bucket','paint-bucket'),
            ('camera','camera'),
            ('bell','bell'),
            ('bolt','bolt'),
            ('star','star'),
            ('heart','heart'),
            ('happy','happy'),
            ('lifesaver','lifesaver'),
            ('rss','rss'),
            ('social','social'),
            ('git-branch','git-branch'),
            ('git-fork','git-fork'),
            ('world','world'),
            ('calendar','calendar'),
            ('clock','clock'),
            ('history','history'),
            ('future','future'),
            ('pencil','pencil'),
            ('trash','trash'),
            ('move','move'),
            ('link','link'),
            ('question','question'),
            ('info','info'),
            ('warning','warning'),
            ('image','image'),
            ('thumbnails','thumbnails'),
            ('table','table'),
            ('list','list'),
            ('menu','menu'),
            ('grid','grid'),
            ('more','more'),
            ('more-vertical','more-vertical'),
            ('plus','plus'),
            ('plus-circle','plus-circle'),
            ('minus','minus'),
            ('minus-circle','minus-circle'),
            ('close','close'),
            ('check','check'),
            ('ban','ban'),
            ('refresh','refresh'),
            ('play','play'),
            ('play-circle','play-circle'),
            ('Devices','Devices'),
            ('tv','tv'),
            ('desktop','desktop'),
            ('laptop','laptop'),
            ('tablet','tablet'),
            ('phone','phone'),
            ('tablet-landscape','tablet-landscape'),
            ('phone-landscape','phone-landscape'),
            ('Storage','Storage'),
            ('file','file'),
            ('copy','copy'),
            ('file-edit','file-edit'),
            ('folder','folder'),
            ('album','album'),
            ('push','push'),
            ('pull','pull'),
            ('server','server'),
            ('database','database'),
            ('cloud-upload','cloud-upload'),
            ('cloud-download','cloud-download'),
            ('download','download'),
            ('upload','upload'),
            ('Direction','Direction'),
            ('reply','reply'),
            ('forward','forward'),
            ('expand','expand'),
            ('shrink','shrink'),
            ('arrow-up','arrow-up'),
            ('arrow-down','arrow-down'),
            ('arrow-left','arrow-left'),
            ('arrow-right','arrow-right'),
            ('chevron-up','chevron-up'),
            ('chevron-down','chevron-down'),
            ('chevron-left','chevron-left'),
            ('chevron-right','chevron-right'),
            ('triangle-up','triangle-up'),
            ('triangle-down','triangle-down'),
            ('triangle-left','triangle-left'),
            ('triangle-right','triangle-right'),
            ('Editor','Editor'),
            ('bold','bold'),
            ('italic','italic'),
            ('strikethrough','strikethrough'),
            ('video-camera','video-camera'),
        )
    en_name = models.CharField(max_length=144)
    es_name = models.CharField(max_length=144)
    en_description = RichTextField(blank=True)
    es_description = RichTextField(blank=True)
    icon = models.CharField(
            choices=ICON_CHOICES,
            null=True,
            blank=True,
            max_length=144
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.es_name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Site values')
        verbose_name_plural = ('Site values')


class Site_info(models.Model):
    """# Website model"""
    LANG_CHOICES = (
            (1,'en'),
            (2,'es'),
        )
    es_name = models.CharField(max_length=144)
    en_name = models.CharField(max_length=144)
    es_description = RichTextField(null=True,blank=True)
    en_description = RichTextField(null=True,blank=True)
    es_mision = RichTextField(null=True,blank=True)
    en_mision = RichTextField(null=True,blank=True)
    es_vision = RichTextField(null=True,blank=True)
    en_vision = RichTextField(null=True,blank=True)
    default_lang = models.PositiveSmallIntegerField(
            choices=LANG_CHOICES,
            null=True,
            blank=True
        )
    logo = models.ImageField(
            upload_to='site',
            null=True, 
            blank=True, 
            width_field="width_field_logo", 
            height_field="height_field_logo"
        )
    logo_sm = models.ImageField(
            upload_to='site',
            null=True, 
            blank=True, 
            width_field="width_field_logo_sm", 
            height_field="height_field_logo_sm"
        )
    logo_lg = models.ImageField(
            upload_to='site',
            null=True, 
            blank=True, 
            width_field="width_field_logo_lg", 
            height_field="height_field_logo_lg"
        )
    mision_img = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True, 
        width_field="width_field_mision_img", 
        height_field="height_field_mision_img"
    )
    vision_img = models.ImageField(
        upload_to='site',
        null=True, 
        blank=True, 
        width_field="width_field_vision_img", 
        height_field="height_field_vision_img"
    )
    width_field_logo = models.IntegerField(default=0)
    height_field_logo = models.IntegerField(default=0)
    width_field_logo_sm = models.IntegerField(default=0)
    height_field_logo_sm = models.IntegerField(default=0)
    width_field_logo_lg = models.IntegerField(default=0)
    height_field_logo_lg = models.IntegerField(default=0)
    width_field_mision_img = models.IntegerField(default=0)
    height_field_mision_img = models.IntegerField(default=0)
    width_field_vision_img = models.IntegerField(default=0)
    height_field_vision_img = models.IntegerField(default=0)
    social_icons = models.ManyToManyField(Socialmedia, blank=True)
    values = models.ManyToManyField(Site_value, blank=True)
    country = models.ManyToManyField(Country, blank=True)
    history = models.ManyToManyField(
        Timeline,
        blank=True,
    )

    def __str__(self):
        return self.en_name

    class Meta:
        verbose_name = ('Site info')
        verbose_name_plural = ('Site info')