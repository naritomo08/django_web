from django.views import generic
from .models import Article
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import SearchForm

class IndexView(generic.ListView):
    model = Article
    template_name = 'bbs/index.html'

class DetailView(generic.DetailView):
    model = Article
    template_name = 'bbs/detail.html'

class CreateView(generic.edit.CreateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = '__all__'

class UpdateView(generic.edit.UpdateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = '__all__'

class DeleteView(generic.edit.DeleteView):
    model = Article
    template_name = 'bbs/delete.html'
    success_url = reverse_lazy('bbs:index')

def search(request):
    articles = None
    searchform = SearchForm(request.GET)

    if searchform.is_valid():
        query = searchform.cleaned_data['query']
        articles = Article.objects.filter(content__icontains=query)
        return render(request, 'bbs/results.html', {'articles': articles, 'searchform': searchform})
