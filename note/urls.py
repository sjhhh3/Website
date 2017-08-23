from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.NoteView.as_view(), name = 'note'),
    url(r'^(?P<pk>\d+)$', views.NotepostView.as_view(), name='notepost'),
    url(r'^None/$', views.NoteNone, name='notenone'),
]

