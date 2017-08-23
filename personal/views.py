from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request,'personal/basic.html')

def profile(request):
    return render(request,'personal/profile.html')

def error404(request):
    return render(request,'personal/404.html')

def error500(request):
    return render(request,'personal/500.html')



