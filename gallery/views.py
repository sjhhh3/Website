from django.shortcuts import render, redirect
from .models import Photo
from .form import CommentCreate

# Create your views here.
def GalleryView(request):
    allphoto = Photo.objects.all().order_by("-date")
    return render(request, 'gallery/gallery.html',{'photo':allphoto})

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

def PhotoView(request,pk):
    photo = Photo.objects.get(pk=pk)
    form = CommentCreate(request.POST)
    if form.is_valid():
        photocomment = form.save(commit=False)
        photocomment.post = photo
        photocomment.address = get_ip(request)
        if (len(photocomment.author) > 11 or len(photocomment.body) > 141 or ("<" in photocomment.body)) is False:
            photocomment.save()
            return redirect('/gallery/success')
        else:
            return redirect('/gallery/None')
    else:
        form = CommentCreate()
        template = 'gallery/photo.html'
        context = {'form': form, 'photo': photo}
        return render(request, template, context)

def GalleryNone(request):
    return render(request,'gallery/None.html')

def SuccessView(request):
    allphoto = Photo.objects.all().order_by("-date")
    return render(request, 'gallery/success.html',{'photo':allphoto})