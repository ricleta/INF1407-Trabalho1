from django.shortcuts import render
from django.views.generic.base import View
from .models import Review
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm

def home_page(request):
    return render(request, 'Reviews/index.html')

def home_page_reviews(request):
    return render(request, 'Reviews/home_page_reviews.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        form = UserCreationForm()
    return render(request, 'Reviews/signup.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ReviewListView(View):
    def get(self, request, *args, **kwargs):
        reviews = Review.objects.filter(user=request.user).order_by('title')
        contexto = {'reviews': reviews}
        return render(request, 'Reviews/listaReviews.html', contexto)

@method_decorator(login_required, name='dispatch')
class ReviewCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = {'formulario': ReviewForm}
        return render(request, 'Reviews/criaReview.html', contexto)

    def post(self, request, *args, **kwargs):
        formulario = ReviewForm(request.POST)
        if formulario.is_valid():
            review = formulario.save(commit=False)
            review.user = request.user
            review.save()
            return HttpResponseRedirect(reverse_lazy('Reviews:lista-reviews'))
        else:
            contexto = {'formulario': formulario, 'mensagem': 'Erro ao criar avaliação. Verifique os dados.'}
            return render(request, 'Reviews/criaReview.html', contexto)

@method_decorator(login_required, name='dispatch')
class ReviewUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        review = Review.objects.get(pk=pk, user=request.user)
        formulario = ReviewForm(instance=review)
        contexto = {'formulario': formulario}
        return render(request, 'Reviews/atualizaReview.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        review = Review.objects.get(pk=pk, user=request.user)
        formulario = ReviewForm(request.POST, instance=review)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('Reviews:lista-reviews'))
        else:
            contexto = {'formulario': formulario, 'mensagem': 'Erro ao atualizar avaliação. Verifique os dados.'}
            return render(request, 'Reviews/atualizaReview.html', contexto)

@method_decorator(login_required, name='dispatch')
class ReviewDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        review = Review.objects.get(pk=pk, user=request.user)
        contexto = {'review': review}
        return render(request, 'Reviews/deletaReview.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        review = Review.objects.get(pk=pk, user=request.user)
        review.delete()
        return HttpResponseRedirect(reverse_lazy('Reviews:lista-reviews'))

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'rating', 'comment']
        labels = {
            'title': 'Título do Jogo/Filme',
            'rating': 'Nota (1 a 10)',
            'comment': 'Comentário',
        }
        help_texts = {
            'title': 'Informe o título do jogo ou filme.',
            'rating': 'Escolha uma nota de 1 a 10.',
            'comment': 'Escreva um comentário sobre o jogo/filme (máx. 500 caracteres).',
        }
        error_messages = {
            'title': {'max_length': 'O título é muito longo.', 'required': 'O título é obrigatório.'},
            'rating': {'required': 'A nota é obrigatória.'},
            'comment': {'max_length': 'O comentário é muito longo.', 'required': 'O comentário é obrigatório.'},
        }