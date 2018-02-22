from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import (Post, Comment)

class Home(ListView):
    model = Post
    # context_object_name = 'boards'
    # queryset = ''
    template_name = 'app/blog.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Ultimas noticias'
        context['has_newsletter'] = True

        return context


class Blog_Detail(DetailView):

    model = Post
    template_name = 'app/detail/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = Comment.objects.all().filter(content_type=17)
        if comments.exists():
            context['has_comments'] = True
            context['comments'] = comments.filter(object_id=context['object'].id)
        else:
            context['has_comments'] = False

        # context['now'] = timezone.now()
        return context