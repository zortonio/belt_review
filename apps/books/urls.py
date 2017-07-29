from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_book_review, name='add'),
    url(r'^process/(?P<route>\w+)$', views.process, name='process'),
    url(r'^(?P<id>\d+)$', views.book_page, name='book_page'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete')
]
