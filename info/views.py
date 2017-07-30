from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article


class ArticleListView(ListView):
    queryset = Article.objects.order_by('-published')
    template_name = 'info/index.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        return super(ArticleListView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        return super(ArticleDetailView, self).get_context_data(**kwargs)


def about_me(request):
    return render(request, 'info/about-me.html')


def portfolio(request):
    return render(request, 'info/portfolio.html')


def contact(request):
    return render(request, 'info/contact.html')
