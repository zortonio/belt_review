from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^validate/(?P<route>\w+)$', views.validate, name='validate'),
    url(r'^users/(?P<id>\d+)$', views.user, name='user')
]
