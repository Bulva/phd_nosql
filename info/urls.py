from django.conf.urls import url
from . import views
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='index'),
    url(r'^article/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^about-me/', views.about_me, name='about me'),
    url(r'^portfolio/', views.portfolio, name='portfolio'),
    url(r'^contact/', views.contact, name='contact'),
]