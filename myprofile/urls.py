from django.conf.urls import url
from . import views # . represents current package

urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.ProfilePostView.as_view(), name='profilepost'),
]
