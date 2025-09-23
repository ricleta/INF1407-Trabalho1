from django.urls import path
from . import views

app_name = 'Reviews'

urlpatterns = [
    path('', views.home_page_reviews, name='home-page-reviews'),
    path('lista/', views.ReviewListView.as_view(), name='lista-reviews'),
    path('cria_review/', views.ReviewCreateView.as_view(), name='cria-review'),
    path('atualiza_review/<int:pk>/', views.ReviewUpdateView.as_view(), name='atualiza-review'),
    path('deleta_review/<int:pk>/', views.ReviewDeleteView.as_view(), name='deleta-review'),
]