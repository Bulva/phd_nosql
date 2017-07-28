from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bio/', views.bio, name='bio'),
    url(r'^skills/', views.skills, name='skills'),
    url(r'^projects/', views.projects, name='projects'),
]