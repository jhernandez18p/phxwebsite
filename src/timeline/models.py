from django.db import models
from ckeditor.fields import RichTextField
from django.template import defaultfilters
from django.utils.text import slugify
import datetime


# Create your models here.
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
        ordering = ["year"]