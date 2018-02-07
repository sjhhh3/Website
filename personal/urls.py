from django.conf.urls import url
from . import views # . represents current package

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^contact/$', views.contact, name = 'contact'),
    url(r'^wmata$', views.wmata, name = 'wmata'),
]
