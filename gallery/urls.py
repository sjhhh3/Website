from django.conf.urls import url
from . import views # . represents current package

urlpatterns = [
    url(r'^$', views.GalleryView, name = 'gallery'),
    url(r'^(?P<pk>\d+)$', views.PhotoView, name='photo'),
    url(r'^None/$', views.GalleryNone, name='gallerynone'),
    url(r'^success/$', views.SuccessView, name='gallerysuccess'),
]
