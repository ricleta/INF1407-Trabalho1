from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import GamesModel
from .forms import GamesForm

def home_page_games(request):
    return render(request, 'Games/home_page_games.html')

class GamesListView(ListView):
    model = GamesModel
    context_object_name = 'games'
    template_name = 'Games/listaGames.html'

class GamesCreateView(CreateView):
    model = GamesModel
    form_class = GamesForm
    template_name = 'Games/criaGames.html'
    success_url = reverse_lazy('Games:lista-games')    

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games_form'] = context['form']
        return super().get_context_data(**kwargs)
    
class GamesUpdateView(UpdateView):
    model = GamesModel
    fields = ['title', 'platforms', 'description', 'release_date', 'developer']
    template_name = 'Games/criaGames.html'
    success_url = reverse_lazy('Games:lista-games')

class GamesDeleteView(DeleteView):
    model = GamesModel
    template_name = 'Games/deletaGames.html'
    success_url = reverse_lazy('Games:lista-games')
