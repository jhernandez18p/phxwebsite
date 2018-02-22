from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify


from ckeditor.fields import RichTextField

from src.utils.libs import (upload_location,get_read_time,count_words)



class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(PostManager, self).filter(draft=False).filter(published__lte=timezone.now())

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE,)
    en_title = models.CharField(max_length=120)
    es_title = models.CharField(max_length=120)
    en_sub_title = models.CharField(max_length=120, blank=True)
    es_sub_title = models.CharField(max_length=120, blank=True)
    en_text = RichTextField()
    es_text = RichTextField()
    draft = models.BooleanField(default=False)
    published = models.DateField(auto_now=True, auto_now_add=False)
    read_time =  models.IntegerField(default=0) # models.TimeField(null=True, blank=True) #assume minutes
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    img = models.ImageField(
        upload_to=upload_location, 
        null=True, 
        blank=True, 
        width_field="img_width_field", 
        height_field="img_height_field",
        default='',
    )
    img_height_field = models.IntegerField(default=0)
    img_width_field = models.IntegerField(default=0)
    background = models.ImageField(
        upload_to=upload_location,
        null=True, 
        blank=True, 
        width_field="background_width_field", 
        height_field="background_height_field",
        default='',
    )
    background_width_field = models.IntegerField(default=0)
    background_height_field = models.IntegerField(default=0)
    en_slug = models.SlugField(unique=True, blank=True)
    es_slug = models.SlugField(unique=True, blank=True)

    objects = PostManager()

    def __unicode__(self):
        return self.en_title

    def __str__(self):
        return self.es_title

    def get_absolute_url_en(self):
        return reverse("en:news_detail", kwargs={"slug": self.en_slug})

    def get_absolute_url_es(self):
        return reverse("es:detalle_noticias", kwargs={"slug": self.es_slug})

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    class Meta:
        ordering = ["-created_at", "-updated"]
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'


def create_slug_en(instance, new_slug=None):
    en_slug = slugify(instance.en_title)
    if new_slug is not None:
        en_slug = new_slug
    qs = Post.objects.filter(en_slug=en_slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(en_slug, qs.first().id)
        return create_slug_en(instance, new_slug=new_slug)
    return en_slug

def create_slug_es(instance, new_slug=None):
    es_slug = slugify(instance.es_title)
    if new_slug is not None:
        es_slug = new_slug
    qs = Post.objects.filter(es_slug=es_slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(es_slug, qs.first().id)
        return create_slug_es(instance, new_slug=new_slug)
    return es_slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.en_slug:
        instance.en_slug = create_slug_en(instance)
    
    if not instance.es_slug:
        instance.es_slug = create_slug_es(instance)

    # if instance.content:
    #     html_string = instance.title
    #     read_time_var = str(html_string)
    #     instance.read_time = read_time_var


pre_save.connect(pre_save_post_receiver, sender=Post)


class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id= obj_id).filter(parent=None)
        return qs


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE,)
    es_content = RichTextField()
    es_content = RichTextField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE,)
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')
    object_id = models.PositiveIntegerField()

    objects = CommentManager()

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse("comments:thread", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("comments:delete", kwargs={"id": self.id})
        
    def children(self): #replies
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True


#Post.objects.all()
#Post.objects.create(user=user, title="Some time")