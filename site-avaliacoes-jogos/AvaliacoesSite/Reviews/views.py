from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Review
from .forms import ReviewForm

from django.http import HttpResponseRedirect
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
class ReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'Reviews/listaReviews.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'Reviews/criaReview.html'
    success_url = reverse_lazy('Reviews:lista-reviews')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'Reviews/atualizaReview.html'
    success_url = reverse_lazy('Reviews:lista-reviews')
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'Reviews/deletaReview.html'
    success_url = reverse_lazy('Reviews:lista-reviews')
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
