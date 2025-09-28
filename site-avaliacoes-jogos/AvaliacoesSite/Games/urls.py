from django.urls import path
from . import views

app_name = 'Games'

urlpatterns = [
    path('', views.GamesHomePageView.as_view(), name='home-page-games'),
    path('lista/', views.GamesListView.as_view(), name='lista-games'),
    path('cria_games/', views.GamesCreateView.as_view(), name='cria-games'),
    path('atualiza_games/<int:pk>/', views.GamesUpdateView.as_view(), name='atualiza-games'),
    path('deleta_games/<int:pk>/', views.GamesDeleteView.as_view(), name='deleta-games'),
]
