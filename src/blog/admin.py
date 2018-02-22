from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import (Comment, Post)
# Register your models here.


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['author',]

    class Meta:
        model = Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["es_title", "updated", "created_at"]
    list_display_links = ["created_at",]
    list_editable = ["es_title"]
    list_filter = ["created_at", "updated"]
    search_fields = ["es_title", "content"]
    # fieldsets = [
    #     (_('Author'), {'fields': ['author','']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [CommentInline,]
    
    class Meta:
        model = Post


admin.site.register(Comment, CommentModelAdmin)
admin.site.register(Post, PostModelAdmin)