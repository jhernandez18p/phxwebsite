from django.contrib import admin

# Register your models here.
from local_apps.blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['en_name',]
    list_display = (
                    'es_name',
                    'es_title',
                    'es_sub_title',
                    'es_description',
                    'es_short_description',
                    'large_image',
                    'short_image',
                )
    class Meta:
        model = Post
