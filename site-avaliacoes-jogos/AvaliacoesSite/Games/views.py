from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import GamesModel
from .forms import GamesForm

class GamesHomePageView(LoginRequiredMixin, ListView):
    '''
    View for displaying the home page of games for the logged-in user.
    '''
    model = GamesModel
    template_name = 'Games/home_page_games.html'
    context_object_name = 'games'

    def get_queryset(self):
        '''
        Returns the queryset of games developed by the logged-in user.
        '''
        return GamesModel.objects.filter(developer=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        '''
        Checks for user authentication and group membership before allowing access.
        '''
        if not request.user.groups.filter(name='GameDev').exists():
            messages.error(request, "Você não tem permissão para visualizar esta página.")
            return HttpResponseRedirect(reverse('home-page'))
        return super().dispatch(request, *args, **kwargs)

class GamesListView(ListView):
    """
    View for displaying a list of all games.

    This view is accessible to all users and lists all games available on the site.
    """
    model = GamesModel
    context_object_name = 'games'
    template_name = 'Games/listaGames.html'


class GamesCreateView(CreateView, LoginRequiredMixin):
    """
    View for creating a new game.

    Only authenticated users belonging to the 'GameDev' group can create games.
    The view automatically sets the 'developer' of the game to the current user.
    """
    model = GamesModel
    form_class = GamesForm
    template_name = 'Games/criaGames.html'
    success_url = reverse_lazy('Games:lista-games')    

    def form_valid(self, form):
        """
        Overrides the form_valid method to associate the logged-in user with the new game.
        """
        form.instance.developer = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Adds the games_form to the context.
        """
        context = super().get_context_data(**kwargs)
        context['games_form'] = context['form']
        return super().get_context_data(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        """
        Checks for user authentication and group membership before allowing access.
        """
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.groups.filter(name='GameDev').exists():
            messages.error(request, "Você não tem permissão para criar jogos.")
            return HttpResponseRedirect(reverse('home-page'))
        return super().dispatch(request, *args, **kwargs)
    
class GamesUpdateView(UpdateView, LoginRequiredMixin):
    """
    View for updating an existing game.

    Only authenticated users belonging to the 'GameDev' group can update games.
    """
    model = GamesModel
    form_class = GamesForm
    template_name = 'Games/criaGames.html'
    success_url = reverse_lazy('Games:lista-games')

    def dispatch(self, request, *args, **kwargs):
        """
        Checks for user authentication and group membership before allowing access.
        """
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.groups.filter(name='GameDev').exists():
            messages.error(request, "Você não tem permissão para atualizar jogos.")
            return HttpResponseRedirect(reverse('home-page'))
        return super().dispatch(request, *args, **kwargs)

class GamesDeleteView(DeleteView, LoginRequiredMixin):
    """
    View for deleting an existing game.

    Only authenticated users belonging to the 'GameDev' group can delete games.
    """
    model = GamesModel
    template_name = 'Games/deletaGames.html'
    success_url = reverse_lazy('Games:lista-games')

    def dispatch(self, request, *args, **kwargs):
        """
        Checks for user authentication and group membership before allowing access.
        """
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.groups.filter(name='GameDev').exists():
            messages.error(request, "Você não tem permissão para deletar jogos.")
            return HttpResponseRedirect(reverse('home-page'))
        return super().dispatch(request, *args, **kwargs)
