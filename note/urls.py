from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.NoteView.as_view(), name = 'note'),
    url(r'^(?P<pk>\d+)$', views.NotepostView.as_view(), name='notepost'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.MonthView, name='notemonth'),
    url(r'^None/$', views.NoteNone, name='notenone'),
]

