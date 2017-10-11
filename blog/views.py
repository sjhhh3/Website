from django.views import generic
from .models import Post, Like
from .form import CommentCreate
from django.shortcuts import render, redirect
import datetime

today = datetime.date.today()
# Create your views here.
class BlogView(generic.ListView):
    template_name = "blog/blog.html"
    context_object_name = "all_post"
    def get_queryset(self):
        return Post.objects.filter(date__year=today.year, date__month=today.month).order_by("-date")[:25]

def MonthView(request, year, month):
    all_posts = Post.objects.filter(date__year=int(year), date__month=int(month)).order_by("-date")[:25]
    if all_posts.exists():
        context = {'all_posts': all_posts}
        return render(request, "blog/blog.html",context)
    return render(request,'blog/None.html')

#class PostView(generic.DetailView):
#    model = Post
#    template_name = 'blog/post.html'
#def PostView(request, pk):
#    post = Post.objects.get(pk=pk)
#    context = {'post':post}
#    return render(request,'blog/post.html',context)

def BlogNone(request):
    return render(request,'blog/None.html')

def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip

def PostView(request, pk):
    post = Post.objects.get(pk=pk)
    like = Like.objects.filter(post=post).count()
    print(like)
    form = CommentCreate(request.POST)
    if form.is_valid():
        blogcomment = form.save(commit=False)
        blogcomment.post = post
        blogcomment.address = get_ip(request)
#        post.ips += blogcomment.address + "\n"
        if (len(blogcomment.author)>11 or len(blogcomment.body)>141 or ("<" in blogcomment.body))is False:
            blogcomment.save()
#            post.save()
            return redirect('/blog/success')
        else:
            return redirect('/blog/None')
    else:
        form = CommentCreate()
        template = 'blog/post.html'
        context = {'form': form, 'post':post}
        return render(request, template, context)

class SuccessView(generic.ListView):
    template_name = "blog/success.html"
    context_object_name = "all_post"
    def get_queryset(self):
        return Post.objects.filter(date__year=today.year, date__month=today.month).order_by("-date")[:25]