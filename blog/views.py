from django.views import generic
from .models import Post
from django.shortcuts import render

# Create your views here.
class BlogView(generic.ListView):
    template_name = "blog/blog.html"
    context_object_name = "all_post"

    def get_queryset(self):
        return Post.objects.all().order_by("-date")[:25]

class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

def BlogNone(request):
    return render(request,'blog/None.html')



