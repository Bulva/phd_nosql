from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .forms import ContactForm


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
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('info/contact.html')
    return render(request, "info/contact.html", {'form': form})
