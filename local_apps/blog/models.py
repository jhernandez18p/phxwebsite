from django.db import models
from django.template import defaultfilters
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify

from local_apps.frontend.models import Sub_category
from local_apps.countries.models import Country

class Post(models.Model):
    es_name = models.CharField(max_length=144)
    en_name = models.CharField(max_length=144)
    es_title = models.CharField(max_length=144,blank=True)
    en_title = models.CharField(max_length=144,blank=True)
    es_slug = models.CharField(max_length=144,blank=True)
    en_slug = models.CharField(max_length=144,blank=True)
    es_sub_title = models.CharField(max_length=144, blank=True)
    en_sub_title = models.CharField(max_length=144, blank=True)
    es_short_description = RichTextField(blank=True)
    en_short_description = RichTextField(blank=True)
    es_description = RichTextField()
    en_description = RichTextField()
    sub_category = models.ForeignKey(
        Sub_category,
        on_delete=models.CASCADE,
        blank=True
    )
    background_image = models.ImageField(
        upload_to='posts/backgrounds/',
        width_field="background_image_height",
        height_field="background_image_width",
        blank=True,
    )
    background_image_height = models.IntegerField(default=0, blank=True,)
    background_image_width = models.IntegerField(default=0, blank=True,)
    large_image = models.ImageField(
        upload_to='posts/images/large/',
        width_field="large_image_height",
        height_field="large_image_width",
        blank=True,
    )
    large_image_height = models.IntegerField(default=0, blank=True,)
    large_image_width = models.IntegerField(default=0, blank=True,)
    short_image = models.ImageField(
        upload_to='posts/images/short/',
        width_field="short_image_height",
        height_field="short_image_width",
        blank=True,
    )
    short_image_height = models.IntegerField(default=0, blank=True,)
    short_image_width = models.IntegerField(default=0, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.en_title

    def get_absolute_url_en(self):
        return reverse("en:news_detail", kwargs={"slug": self.en_slug})

    def get_absolute_url_es(self):
        return reverse("es:detalle_noticias", kwargs={"slug": self.es_slug})

    def es_get_unique_slug(self):
        slug = slugify(self.es_title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(es_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def en_get_unique_slug(self):
        slug = slugify(self.en_title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(en_slug=unique_slug).exists():
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
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')
        ordering = ["-created_at"]
