from django.urls import (path, re_path, include)
from .views import (
    Home,
    Blog_Detail,
)

app_name = 'blog'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('/<slug:slug>', Blog_Detail.as_view(), name='blog_detail'),
]