from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^summary/$', views.summary, name='summary'),
    url(r'^skrabani/$', views.ScratchingList.as_view(), name='skrabani'),
]