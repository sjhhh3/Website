from django.shortcuts import render, redirect
from django.views import generic
from .models import Comment
from .form import CommentCreate
from django.views.generic.edit import CreateView

# Create your views here.

#class CommentCreate(CreateView):
 #   model = Comment
  #  fields = ['author','date','body','published']

def BoardView(request):
    allcomment = Comment.objects.all().order_by("-date")
    return render(request, 'board/board.html',{'comment':allcomment})

def SuccessView(request):
    allcomment = Comment.objects.all().order_by("-date")
    return render(request, 'board/success.html',{'comment':allcomment})

def FailView(request):
    allcomment = Comment.objects.all().order_by("-date")
    return render(request, 'board/fail.html',{'comment':allcomment})

def create(request):
    form = CommentCreate(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        if (len(comment.author)>11 or len(comment.body)>141 or ("<" in comment.body))is False:
            comment.save()
            return redirect('/board/success')
        else:
            return redirect('/board/fail')
    else:
        form = CommentCreate()
        template = 'board/comment_form.html'
        context = {'form': form}
        return render(request, template, context)