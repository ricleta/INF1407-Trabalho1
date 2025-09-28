from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Review
from .forms import ReviewForm
from django.contrib.auth.models import Group

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

def home_page(request):
    return render(request, 'Reviews/index.html')

class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'Reviews/listaReviews.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.groups.filter(name='Reviewers').exists():
            return HttpResponseRedirect(reverse('home-page'))
        return super().dispatch(request, *args, **kwargs)

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'Reviews/criaReview.html'
    success_url = reverse_lazy('Reviews:lista-reviews')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.groups.filter(name='Reviewers').exists():
            return HttpResponseRedirect(reverse('home-page'))
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'Reviews/atualizaReview.html'
    success_url = reverse_lazy('Reviews:lista-reviews')
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'Reviews/deletaReview.html'
    success_url = reverse_lazy('Reviews:lista-reviews')
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
