from django.conf.urls import url, include
# from django.views.generic import ListView, DetailView . represents current package
# from blog.models import Post
from . import views

app_name = 'blog'

urlpatterns = [
    #ListView.as_view(queryset=Post.objects.all() .order_by("-date")[:25], template_name = "blog/blog.html"
    url(r'^$', views.BlogView.as_view(), name = 'blog'),
    url(r'^(?P<pk>\d+)$', views.PostView.as_view(), name='post'),
    url(r'^None/$',views.BlogNone, name = 'blognone'),
    #DetailView.as_view(model=Post, template_name = "blog/post.html")
]

