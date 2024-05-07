from django.views import generic
from .models import Article

class IndexView(generic.ListView):
    model = Article
    template_name = 'bbs/index.html'

class DetailView(generic.DetailView):
    model = Article
    template_name = 'bbs/detail.html'
