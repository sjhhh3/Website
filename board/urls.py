from django.conf.urls import url
from . import views # . represents current package

urlpatterns = [
    url(r'^$', views.BoardView, name = 'board'),
    url(r'^add/$', views.create, name = 'commentcreate'),
    url(r'^success/$', views.SuccessView, name='success'),
    url(r'^fail/$', views.FailView, name='fail'),
]
